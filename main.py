from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

class Numbers(BaseModel):
    num1: float
    num2: float

class User(BaseModel):
    name: str
    id: int

class UserWithAge(BaseModel):
    name: str
    age: int

user1 = User(name="Иван Иванов", id=1)

app = FastAPI()

# Маршруты
@app.get("/info")
async def root():
    return {"message": "Автореалоад действительно работает"}

@app.get("/")
async def get_html():
    return FileResponse("index.html")

@app.post("/calculate")
async def calculate(nums: Numbers):
    return {"result": nums.num1 + nums.num2}

@app.get("/users")
async def get_user():
    return user1

@app.post("/user")
async def check_user(user: UserWithAge):
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": user.age >= 18
    }

from models import Feedback
from feedback_data import feedbacks

@app.post("/feedback")
async def post_feedback(fb: Feedback):
    feedbacks.append(fb.model_dump())
    return {"message": f"Спасибо, {fb.name}! Ваш отзыв сохранён."}