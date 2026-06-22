import sqlite3
from fastapi import FastAPI

app = FastAPI()

connection = sqlite3.connect("database.db", check_same_thread=False)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS todo(
    id INTEGER PRIMARY KEY ,
    title TEXT,
    completed BOOLEAN DEFAULT FALSE
    )
""")

connection.commit()

@app.get("/")
def home():
    return {"message": "Welcome to the Todo API!"
    "SQLite connected successfully."}