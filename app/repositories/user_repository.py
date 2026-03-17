from uuid import UUID

from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, user: User):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get_by_id(self, user_id: UUID):
        return (
            self.session.query(User)
            .filter(User.id == user_id)
            .first()
        )

    def get_all(self):
        return self.session.query(User).all()

    def update(self, user: User):
        self.session.commit()
        self.session.refresh(user)
        return user

    def delete(self, user_id: UUID):
        user = self.get_by_id(user_id) # fetch the project to delete

        if not user:
            return None
        self.session.delete(user)
        self.session.commit()
        return user
