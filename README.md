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

## Created by Nicholas Lee
