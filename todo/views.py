from fastapi import FastAPI, Depends
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


# Get All Todos
@app.get('/')
async def read_all(db: Session = Depends(get_db)):
    return db.query(models.Todo).all()
