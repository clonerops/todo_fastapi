from typing import Optional

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse

import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


# Config Database
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# Class Todos For Post Request
class Todo(BaseModel):
    title: str
    description: Optional[str]
    priority: int = Field(gt=0, lt=100, description="The priority must between 1-99")
    complete: bool


# Get All Todos
@app.get('/todo')
async def read_all_todo(db: Session = Depends(get_db)):
    return db.query(models.Todos).all()


# Get Todos By Id
@app.get('/todo/{todo_id}')
async def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo_model = db.query(models.Todos).filter(models.Todos.Id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail="Todo not found")


# Post Todos Request
@app.post('/todo')
async def create_todo(todo: Todo, db: Session = Depends(get_db)):
    todo_model = models.Todos()
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete

    db.add(todo_model)
    db.commit()

    return JSONResponse(status_code=201, content="successful")


# Put Todos Request
@app.put('/todo/{todo_id}')
async def update_todo(todo_id: int, todo: Todo, db: Session = Depends(get_db)):
    todo_update_model = db.query(models.Todos) \
        .filter(models.Todos.Id == todo_id) \
        .first()
    print(todo_update_model)
    if todo_update_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo_update_model.title = todo.title
    todo_update_model.description = todo.description
    todo_update_model.priority = todo.priority
    todo_update_model.complete = todo.complete

    db.add(todo_update_model)
    db.commit()

    return JSONResponse(status_code=200, content='success')


# Delete Todos Request
@app.delete('/todo/{todo_id}')
async def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo_delete_model = db.query(models.Todos) \
        .filter(models.Todos.Id == todo_id) \
        .first()
    if todo_delete_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(todo_delete_model)
    db.commit()

    return JSONResponse(status_code=200, content='success')
