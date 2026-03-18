from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.repositories.task_repository import TaskRepository
from app.schemas.task_schema import TaskResponse
from app.services.task_service import TaskService

router = APIRouter()

@router.post("/ai/description")
def generate_description(
    task_id: UUID,
    db: Session = Depends(get_db)
):
    repo = TaskRepository(db)
    service = TaskService(repo)

    service.description_generator(task_id)

    return {"message": "The description is generated successfully"}

