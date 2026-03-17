from uuid import UUID

from sqlalchemy.orm import Session

from app.models.task import Task


class TaskRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, task: Task):
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        return task

    def get_all(self):
        return self.session.query(Task).all()

    def get_task_by_id(self, task_id: UUID):
        return (
            self.session.query(Task)
            .filter(Task.id == task_id)
            .first()
        )

    def update(self, task: Task):
        self.session.commit()
        self.session.refresh(task)
        return task

    def delete(self, task_id: UUID):
        task = self.get_task_by_id(task_id)
        if not task:
            return None

        self.session.delete(task)
        self.session.commit()
        return task