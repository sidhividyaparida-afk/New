from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# class User(BaseModel):
#     name: str
#     age: int

# @app.post("/new user")
# def new_user(user: User):
#     return{
#         "message": "User created successfully",
#         "data": user
#          }

@app.post("/new user")
def new_user():
    return{
        "message": "User created successfully",
        "data": {"name": str,
                 "king": str
                 }
                 }