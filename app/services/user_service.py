from uuid import UUID

from fastapi import HTTPException
from starlette import status

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate, UserResponse


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo


    def create_user(self, user_data: UserCreate):
        new_user = User(**user_data.model_dump())
        return UserResponse.model_validate(self.repo.create(new_user))


    def get_by_id(self, user_id: UUID):
        user = self.repo.get_by_id(user_id)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        return UserResponse.model_validate(user)


    def get_all(self):
        return [
            UserResponse.model_validate(u) for u in self.repo.get_all()
        ]

    def delete(self, user_id: UUID):
        deleted_user = self.repo.delete(user_id)

        if not deleted_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project Not found"
            )

        return UserResponse.model_validate(deleted_user)
