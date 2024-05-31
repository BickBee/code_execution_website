from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import scipy as sp
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import io
import contextlib

app = FastAPI()

# Add CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this as needed, e.g., ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = "sqlite:///./test.db"
engine = sa.create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class CodeExecution(Base):
    __tablename__ = "code_executions"
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    code = sa.Column(sa.String, index=True)
    output = sa.Column(sa.String)

Base.metadata.create_all(bind=engine)

class CodeRequest(BaseModel):
    code: str

@app.post("/execute")
def execute_code(request: CodeRequest):
    try:
        # Create a StringIO object to capture output
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            exec_globals = {"pd": pd, "sp": sp}
            exec(request.code, exec_globals)
        output = f.getvalue()
        return {"output": output}
    except Exception as e:
        return {"output": str(e)}

@app.post("/submit")
def submit_code(request: CodeRequest):
    try:
        # Create a StringIO object to capture output
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            exec_globals = {"pd": pd, "sp": sp}
            exec(request.code, exec_globals)
        output = f.getvalue()
        db = SessionLocal()
        code_execution = CodeExecution(code=request.code, output=output)
        db.add(code_execution)
        db.commit()
        db.refresh(code_execution)
        return {"message": "Code submitted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
