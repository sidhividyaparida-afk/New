from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()
# Reusable dependency
def get_current_user():
    return {"username": "testuser"}

@app.get("/users")
def users(user = Depends(get_current_user)):
    return {"user": user}

@app.get("/items")
def items(user = Depends(get_current_user)):
    return {"items": ["item1", "item2"], "user": user}

# Authentication
def get_token_header(token: str = Header(None)):
    if token != "fake-super-secret-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"token": token, "User": "Apple"}

@app.get("/secure-data")
def secure_data(token_data = Depends(get_token_header)):
    return {"secure_data": "This is protected data", "token_data": token_data}