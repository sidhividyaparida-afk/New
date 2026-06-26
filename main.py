from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False})

sessionLocal = sessionmaker(bind=engine)

base = declarative_base()

class Todo(base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    completed = Column(String)
base.metadata.create_all(bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/todos")
def create_todo(title: str, description: str, db: Session = Depends(get_db)):
    todo = Todo(title=title, description=description, completed="False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {"message": "Todo created successfully", "todo": todo}