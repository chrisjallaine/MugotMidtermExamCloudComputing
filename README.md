# MugotMidtermExamCloudComputing

## 📌 To-Do List App (FastAPI)
A simple To-Do List web application built with **FastAPI** and **JavaScript (Axios)** for managing user authentication and tasks.

## 🚀 Features
- User Registration & Login
- Secure Password Hashing (bcrypt)
- Create & Retrieve Tasks
- CSV-based Data Storage (users.csv & tasks.csv)
- Frontend Integration with HTML & JavaScript (Axios)

## 🛠️ Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/chrisjallaine/MugotMidtermExamCloudComputing.git
cd MugotMidtermExamCloudComputing
```

### 2️⃣ Install Dependencies
```sh
pip install fastapi uvicorn passlib[bcrypt]
```

### 3️⃣ Run the Server
```sh
uvicorn main:app --reload
```

## 📁 Project Structure
```
MugotMidtermExamCloudComputing/
│── 
│   ├── main.py         # FastAPI Backend
│   ├── data/
│   │   ├── users.csv   # User storage
│   │   ├── tasks.csv   # Task storage
│   ├── index.html      # Login Page
│   ├── register.html   # User Registration Page
│   ├── main.html       # Task Dashboard
│   ├── create_task.html # Task Creation Page
│── README.md           # Documentation
```

## 🔗 API Endpoints
| Method | Endpoint        | Description |
|--------|---------------|-------------|
| POST   | `/create_user/` | Register a new user |
| POST   | `/login/`      | Authenticate a user |
| POST   | `/create_task/` | Create a new task |
| GET    | `/get_tasks/`  | Retrieve tasks for a user |

## 🌐 Frontend Integration
- Uses **Axios** for API requests.
- Stores session data using browser cookies.

## 📜 License
This project is for educational purposes. Feel free to modify and improve!

---
