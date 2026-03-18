from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.repositories.project_repository import ProjectRepository
from app.repositories.task_repository import TaskRepository
from app.repositories.user_repository import UserRepository
from app.schemas.task_schema import TaskCreate, TaskUpdate
from app.services.task_service import TaskService

router = APIRouter()

@router.post("/tasks")
def create_task(
        data: TaskCreate,
        db: Session = Depends(get_db)
):
    repo_task = TaskRepository(db)
    repo_project = ProjectRepository(db)
    repo_user = UserRepository(db)
    service = TaskService(repo_task, repo_project, repo_user)
    return service.create_task(data)


@router.get("/tasks")
def get_all(
        db: Session = Depends(get_db)
):
    repo_task = TaskRepository(db)
    repo_project = ProjectRepository(db)
    repo_user = UserRepository(db)
    service = TaskService(repo_task, repo_project, repo_user)
    return service.get_all()


@router.get("/task/{task_id}")
def get_by_id(
        task_id: UUID,
        db: Session = Depends(get_db)
):
    repo_task = TaskRepository(db)
    repo_project = ProjectRepository(db)
    repo_user = UserRepository(db)
    service = TaskService(repo_task, repo_project, repo_user)
    return service.get_by_id(task_id)

@router.put("/task/{task_id}")
def update(
        data: TaskUpdate,
        task_id: UUID,
        db: Session = Depends(get_db)
):
    repo_task = TaskRepository(db)
    repo_project = ProjectRepository(db)
    repo_user = UserRepository(db)
    service = TaskService(repo_task, repo_project, repo_user)
    return service.update(task_id, data)


@router.delete("/task/{task_id}")
def delete(
        task_id: UUID,
        db: Session = Depends(get_db)
):
    repo_task = TaskRepository(db)
    repo_project = ProjectRepository(db)
    repo_user = UserRepository(db)
    service = TaskService(repo_task, repo_project, repo_user)
    return service.delete(task_id)