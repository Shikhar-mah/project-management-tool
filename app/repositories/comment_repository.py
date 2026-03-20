from uuid import UUID
from sqlalchemy.orm import Session
from app.models.comment import Comment

class CommentRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, comment: Comment):
        self.session.add(comment)
        self.session.commit()
        self.session.refresh(comment)
        return comment

    def get_all(self):
        return self.session.query(Comment).all()

    def get_by_id(self, comment_id: UUID):
        return self.session.query(Comment).filter(Comment.id == comment_id).first()

    def get_by_task_id(self, task_id: UUID):
        return self.session.query(Comment).filter(Comment.task_id == task_id).all()

    def update(self, comment: Comment):
        self.session.commit()
        self.session.refresh(comment)
        return comment

    def delete(self, comment_id: UUID):
        comment = self.get_by_id(comment_id)
        if not comment:
            return None
        self.session.delete(comment)
        self.session.commit()
        return comment