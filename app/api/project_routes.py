from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.repositories.project_repository import ProjectRepository
from app.schemas.project_schema import ProjectCreate, ProjectUpdate
from app.services.project_service import ProjectService

router = APIRouter()

@router.post("/projects")
def create_project(
        data: ProjectCreate,
        db: Session = Depends(get_db)
):
    repo = ProjectRepository(db)
    service = ProjectService(repo)
    return service.create_project(data)


@router.get("/projects")
def get_all(
        # data: ProjectCreate,
        db: Session = Depends(get_db)
):
    repo = ProjectRepository(db)
    service = ProjectService(repo)
    return service.get_all()


@router.get("/project/{project_id}")
def get_by_id(
        project_id: UUID,
        db: Session = Depends(get_db)
):
    repo = ProjectRepository(db)
    service = ProjectService(repo)
    return service.get_by_id(project_id)

@router.put("/project/{project_id}")
def update(
        data: ProjectUpdate,
        project_id: UUID,
        db: Session = Depends(get_db)
):
    repo = ProjectRepository(db)
    service = ProjectService(repo)
    return service.update(id, data)


@router.delete("/project/{project_id}")
def delete(
        project_id: UUID,
        db: Session = Depends(get_db)
):
    repo = ProjectRepository(db)
    service = ProjectService(repo)
    return service.delete(project_id)