from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate
from app.services.user_service import UserService

router = APIRouter()

@router.post("/users")
def create_user(
        data: UserCreate,
        db: Session = Depends(get_db)
):
    repo = UserRepository(db)
    service = UserService(repo)
    return service.create_user(data)


@router.get("/users")
def get_all(
        db: Session = Depends(get_db)
):
    repo = UserRepository(db)
    service = UserService(repo)
    return service.get_all()


@router.get("/user/{user_id}")
def get_by_id(
        user_id: UUID,
        db: Session = Depends(get_db)
):
    repo = UserRepository(db)
    service = UserService(repo)
    return service.get_by_id(user_id)


@router.delete("/user/{user_id}")
def delete(
        user_id: UUID,
        db: Session = Depends(get_db)
):
    repo = UserRepository(db)
    service = UserService(repo)
    return service.delete(user_id)


"""
There is not really any need to update the users. So not implementing the update user 
api. But if it's still necessary, here is how you would do it. Also you need to add 
the update methods in schemas, services and repositories

@router.post("/user/{id}")
def update(
        data: UserUpdate,
        db: Session = Depends(get_db)
):
    repo = UserRepository(db)
    service = UserService(repo)
    return service.update(data)
"""