from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.repositories.task_repository import TaskRepository
from app.schemas.task_schema import TaskCreate, TaskUpdate
from app.services.task_service import TaskService

router = APIRouter()

@router.post("/tasks")
def create_task(
        data: TaskCreate,
        db: Session = Depends(get_db)
):
    repo = TaskRepository(db)
    service = TaskService(repo)
    return service.create_task(data)


@router.get("/tasks")
def get_all(
        db: Session = Depends(get_db)
):
    repo = TaskRepository(db)
    service = TaskService(repo)
    return service.get_all()


@router.get("/task/{id}")
def get_by_id(
        task_id: UUID,
        db: Session = Depends(get_db)
):
    repo = TaskRepository(db)
    service = TaskService(repo)
    return service.get_by_id(task_id)

@router.post("/task/{id}")
def update(
        data: TaskUpdate,
        db: Session = Depends(get_db)
):
    repo = TaskRepository(db)
    service = TaskService(repo)
    return service.update(data)


@router.post("/task/{id}")
def delete(
        task_id: UUID,
        db: Session = Depends(get_db)
):
    repo = TaskRepository(db)
    service = TaskService(repo)
    return service.delete(task_id)