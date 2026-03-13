from fastapi import FastAPI, HTTPException
app = FastAPI()

from app.db import engine
print(engine)