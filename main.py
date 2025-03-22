import csv
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from passlib.context import CryptContext

# Initialize FastAPI
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Data files
USER_FILE = "data/users.csv"
TASK_FILE = "data/tasks.csv"

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

# User model
class User(BaseModel):
    username: str
    password: str

# Task model
class Task(BaseModel):
    task: str
    deadline: str
    user: str

# Helper functions
def read_csv(file):
    if not os.path.exists(file):
        return []
    with open(file, "r", newline="", encoding="utf-8") as f:
        return list(csv.reader(f))

def write_csv(file, data):
    with open(file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)

# Create user
@app.post("/create_user/")
async def create_user(user: User):
    users = read_csv(USER_FILE)
    for u in users:
        if u[0] == user.username:
            raise HTTPException(status_code=400, detail="User already exists")
    users.append([user.username, pwd_context.hash(user.password)])
    write_csv(USER_FILE, users)
    return {"status": "User Created"}

# User login
@app.post("/login/")
async def user_login(user: User):
    users = read_csv(USER_FILE)
    for u in users:
        if u[0] == user.username and pwd_context.verify(user.password, u[1]):
            return {"status": "Logged in"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

# Create task
@app.post("/create_task/")
async def create_task(task: Task):
    users = read_csv(USER_FILE)
    if not any(u[0] == task.user for u in users):
        raise HTTPException(status_code=400, detail="User does not exist")
    tasks = read_csv(TASK_FILE)
    tasks.append([task.task, task.deadline, task.user])
    write_csv(TASK_FILE, tasks)
    return {"status": "Task Created"}

# Get tasks
@app.get("/get_tasks/")
async def get_tasks(name: str):
    tasks = read_csv(TASK_FILE)
    user_tasks = [[t[0], t[1]] for t in tasks if t[2] == name]
    return {"tasks": user_tasks}
