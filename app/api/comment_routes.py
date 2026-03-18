from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.repositories.comment_repository import CommentRepository
from app.schemas.comment_schema import CommentCreate
from app.services.comment_service import CommentService

router = APIRouter()

@router.post("/comments")
def create_comment(data: CommentCreate, db: Session = Depends(get_db)):
    repo = CommentRepository(db)
    service = CommentService(repo)
    return service.create_comment(data)