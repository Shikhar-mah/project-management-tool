from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends, FastAPI
from sqlalchemy.orm import Session

from app.db import get_db
from app.repositories.project_repository import ProjectRepository
from app.repositories.task_repository import TaskRepository
from app.repositories.user_repository import UserRepository
from app.schemas.task_schema import TaskResponse
from app.services.task_service import TaskService

router = APIRouter()

@router.post("/ai/generate")
def assign_description_priority(
    task_id: UUID,
    db: Session = Depends(get_db)
):
    repo_task = TaskRepository(db)
    repo_project = ProjectRepository(db)
    repo_user = UserRepository(db)
    service = TaskService(repo_task, repo_project, repo_user)

    service.description_generator_priority(task_id)
    task = service.get_by_id(task_id)

    return [
        {"message": "The description and priority is generated successfully"},
        {"updated task": TaskResponse.model_validate(task)}
    ]


# @router.post("/ai/description")
# def generate_description(
#     task_id: UUID,
#     db: Session = Depends(get_db)
# ):
#     repo_task = TaskRepository(db)
#     repo_project = ProjectRepository(db)
#     repo_user = UserRepository(db)
#     service = TaskService(repo_task, repo_project, repo_user)
#
#     service.description_generator(task_id)
#
#     return {"message": "The description is generated successfully"}