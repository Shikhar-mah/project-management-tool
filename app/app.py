from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.db import Base, engine
from app.models import comment, project, task, user
from app.api import ai_routes, comment_routes, project_routes, task_routes, user_routes
app = FastAPI()

app.include_router(project_routes.router)
app.include_router(task_routes.router)
app.include_router(user_routes.router)
app.include_router(comment_routes.router)
app.include_router(ai_routes.router)

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
