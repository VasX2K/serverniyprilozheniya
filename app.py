from fastapi import FastAPI
from starlette.responses import FileResponse
from pydantic import BaseModel, field_validator
from typing import List
import re

app = FastAPI()

# ==================== Задание 1.1 ====================
@app.get("/")
def root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}


# ==================== Задание 1.2 ====================
@app.get("/html")
def html_page():
    return FileResponse("index.html")


# ==================== Задание 1.3* ====================
class CalculateInput(BaseModel):
    num1: float
    num2: float


@app.post("/calculate")
def calculate(data: CalculateInput):
    result = data.num1 + data.num2
    return {"result": result}


# ==================== Задание 1.4 ====================
class User(BaseModel):
    name: str
    id: int


user_instance = User(name="Иван Иванов", id=1)


@app.get("/users")
def get_users():
    return user_instance


# ==================== Задание 1.5* ====================
class UserWithAge(BaseModel):
    name: str
    age: int


@app.post("/user")
def check_adult(user: UserWithAge):
    is_adult = user.age >= 18
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult
    }


# ==================== Задание 2.1 ====================
class Feedback(BaseModel):
    name: str
    message: str


feedbacks: List[Feedback] = []


@app.post("/feedback")
def submit_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    return {"message": f"Feedback received. Thank you, {feedback.name}."}


# ==================== Задание 2.2* ====================
FORBIDDEN_WORDS = ["кринж", "рофл", "вайб"]


class FeedbackValidated(BaseModel):
    name: str
    message: str

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        if len(v) < 2 or len(v) > 50:
            raise ValueError("Имя должно быть от 2 до 50 символов")
        return v

    @field_validator("message")
    @classmethod
    def validate_message(cls, v: str) -> str:
        if len(v) < 10 or len(v) > 500:
            raise ValueError("Сообщение должно быть от 10 до 500 символов")
        
        pattern = r"\b(" + "|".join(FORBIDDEN_WORDS) + ")[а-яА-Я]*\b"
        if re.search(pattern, v, re.IGNORECASE):
            raise ValueError("Использование недопустимых слов")
        return v


feedbacks_validated: List[FeedbackValidated] = []


@app.post("/feedback/validated")
def submit_feedback_validated(feedback: FeedbackValidated):
    feedbacks_validated.append(feedback)
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}
