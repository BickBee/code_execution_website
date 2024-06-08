Hello! In this repo is the code for a website with a code execution environment for Python 3. The code can be put in the Monaco code editor workspace and you can see the resulting code be printed when the "Test Code" button is hit. The code can additionally be saved to your local machine (in a local sqlite database file) by hitting the "submit" button.

This website was made using React (Vite), Typescript, and Tailwind CSS for the frontend, and uses Python and FastAPI for the backend.

Here is how to setup your local machine to run this Python 3 code executor:

Start the backend:
- Clone this repo
- cd backend
- python -m venv venv
- .\venv\Scripts\activate (For Windows)
- pip install -r requirements.txt
- uvicorn main:app --reload

Start the frontend:
- cd frontend
- npm run dev

If anything goes wrong, I also attached a picture of the working website in this repo named "Project Demo".

Created By: Nicholas Lee