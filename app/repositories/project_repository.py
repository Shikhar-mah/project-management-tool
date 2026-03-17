from typing import Optional
from uuid import UUID
from sqlalchemy.orm import Session
from app.models.project import Project

class ProjectRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, project: Project):
        self.session.add(project)
        self.session.commit()
        self.session.refresh(project)
        return project

    def get_by_id(self, project_id: UUID) -> Optional[Project]:
        project = (
            self.session.query(Project)
            .filter(Project.id == project_id)
            .first()
        )

        if not project:
            return None
        return project

    def get_all(self):
        return self.session.query(Project).all()

    def update(self, project_id: UUID, updated_data: dict):
        project = self.get_by_id(project_id)

        if not project:
            return None

        for key, value in updated_data.items():
            setattr(project, key, value)
        self.session.commit()
        self.session.refresh(project)
        return project

    def delete(self, project_id: UUID):
        project = self.get_by_id(project_id) # fetch the project to delete

        if not project:
            return None
        self.session.delete(project)
        self.session.commit()
        return project

    # def get_name_by_id(self, project_id: UUID):
    #     project = self.get_by_id(UUID)
    #     if not project:
    #         return None
    #
    #