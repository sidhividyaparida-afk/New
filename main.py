from fastapi import FastAPI, status, HTTPException

app = FastAPI()

@app.post("/new user", status_code=status.HTTP_201_CREATED)
def create_user():
    return {"message": "User created successfully!"}

@app.get("/users")
def get_users():
    return{
        "status": "success",
        "message": "Users retrieved successfully!"
    }

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id != 666:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    return {
        "id" : user_id,
        "message": "Welcome!",
        "Name": "Castel of Sweets"
    }