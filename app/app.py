from fastapi import FastAPI, HTTPException

from app.db import Base, engine
from app.models import comment, project, task, user
app = FastAPI()

Base.metadata.create_all(bind=engine)