## This file must define 3 things
#1. engine
#2. sessionmaker
#3. Base

# Import these following libraries
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import DATABASE_URL

# Step 1: Engine
# Engine is the connection to PostgreSQL
engine = create_engine(DATABASE_URL)

# Step 2: Session Local
# This creates database sessions per request
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Step 3: Base
# Every model will inherit this
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()