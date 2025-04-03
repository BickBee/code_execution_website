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

# 🐍 Web-Based Python Code Execution Environment

Welcome to the Web-Based Python Code Execution Environment! This platform allows users to write, execute, and save Python 3 code directly from their web browser. Designed with an intuitive interface and robust backend, it streamlines your coding experience.

---

## 📘 About

This project is a **web-based Python code execution environment** that allows users to write, run, and save Python 3 code directly from their browser. It features a sleek and responsive frontend built with **React**, **TypeScript**, and **Tailwind CSS**, alongside a secure backend powered by **FastAPI** and **Python**. All code and results are stored using **SQLite**, enabling persistent local storage. Whether you're experimenting with Python, teaching, or building interactive coding tools, this platform offers a simple, yet powerful solution. 🖥️🐍

---

## ✨ Features

- **Write and Execute Code:** Craft and run Python 3 scripts seamlessly within the web interface.
- **Save Your Work:** Securely save your scripts for future reference and continued development.
- **User-Friendly Interface:** Enjoy a responsive and intuitive frontend built with modern technologies.

---

## 🛠️ Technologies Used

- **Frontend:** React (Vite), TypeScript, Tailwind CSS
- **Backend:** Python, FastAPI
- **Database:** SQLite (local storage)

---

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

Ensure you have the following installed:

- [Node.js](https://nodejs.org/)
- [Python 3.x](https://www.python.org/downloads/)

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/BickBee/code_execution_website.git

2. **Start the Backend:**
   ```bash
   cd backend
   python -m venv venv
   # Activate the virtual environment (Windows)
   .\venv\Scripts\activate
   pip install -r requirements.txt
   uvicorn main:app --reload

3. **Start the Frontend:**
   ```bash
   cd ../frontend
   npm install
   npm run dev

## 🖥️ Usage

Write Code: Use the code editor to type your Python scripts.
Execute: Click the "Run" button to execute your code. The output will be displayed below the editor.
Save: Use the "Save" option to store your scripts for future reference.

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🔒 Security

The code execution environment is sandboxed to prevent malicious code from accessing system resources. However, use at your own risk.

---

## 📞 Contact

For questions or feedback, please open an issue in the GitHub repository.
