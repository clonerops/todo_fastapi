from fastapi import FastAPI
from todo import models
from todo.database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get('/')
async def create_database():
    return {'Databse': 'Created'}
