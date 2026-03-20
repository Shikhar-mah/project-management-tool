from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from app.db import get_db
from app.repositories.comment_repository import CommentRepository
from app.schemas.comment_schema import CommentCreate, CommentResponse
from app.services.comment_service import CommentService

router = APIRouter()

@router.post("/comments")
def create_comment(data: CommentCreate, db: Session = Depends(get_db)):
    repo = CommentRepository(db)
    service = CommentService(repo)
    return service.create_comment(data)

# NEW: GET all comments
@router.get("/comments", response_model=list[CommentResponse])
def get_all_comments(db: Session = Depends(get_db)):
    repo = CommentRepository(db)
    comments = repo.get_all()
    return [CommentResponse.model_validate(c) for c in comments]

# Optional: GET comments by task ID
@router.get("/tasks/{task_id}/comments", response_model=list[CommentResponse])
def get_comments_by_task(task_id: UUID, db: Session = Depends(get_db)):
    repo = CommentRepository(db)
    comments = repo.get_by_task_id(task_id)  # You need to add this method
    return [CommentResponse.model_validate(c) for c in comments]