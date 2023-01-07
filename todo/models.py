from sqlalchemy import Column, Boolean, Integer, String
from database import Base


class Todo(Base):
    __tablename__ = 'todos'

    Id = Column(Integer, index=True, primary_key=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
