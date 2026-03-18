from app.models.comment import Comment
from app.repositories.comment_repository import CommentRepository
from app.schemas.comment_schema import CommentCreate, CommentResponse

class CommentService:
    def __init__(self, repo: CommentRepository):
        self.repo = repo

    def create_comment(self, data: CommentCreate):
        new_comment = Comment(**data.model_dump())
        return CommentResponse.model_validate(self.repo.create(new_comment))