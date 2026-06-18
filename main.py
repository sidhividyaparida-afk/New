from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    name: str
    age: int
    password: str

class UserResponse(BaseModel):
    name: str
    age: int

@app.post("/new_user")
def new_user(user: User):
    users.append(user)
    return {
        "message": "User created successfully",
        "data": user
    }

@app.get("/users", response_model=list[UserResponse])
def get_users():
    return users
