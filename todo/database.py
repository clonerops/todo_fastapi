from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///../todo.db'

# First Step:  Create Sql Alchemy Engine for this step we need use import create_engine from sqlalchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# Two Step: We need to create local session instance for this step we need to import session maker from sqlalchemy.orm
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Three Step: We need create base, base allow us to create each database model for this step we need to import
# declarative_base from sqlalchemy.ext.declarative
Base = declarative_base()
