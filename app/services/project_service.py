from uuid import UUID

from app.repositories.project_repository import ProjectRepository
from app.models.project import Project
from app.schemas.project_schema import ProjectCreate, ProjectUpdate, ProjectResponse
from fastapi import HTTPException, status


class ProjectService:
    def __init__(self, repo: ProjectRepository):
        self.repo = repo


    def create_project(self, project_data: ProjectCreate):
        new_project = Project(**project_data.model_dump())
        return ProjectResponse.model_validate(self.repo.create(new_project))


    def get_by_id(self, project_id: UUID):
        project = self.repo.get_by_id(project_id)

        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found"
            )

        return ProjectResponse.model_validate(project)


    def get_all(self):
        return [
            ProjectResponse.model_validate(p) for p in self.repo.get_all()
        ]

    def update(self, project_id: UUID, updated_details: ProjectUpdate):
        if not updated_details.model_dump(exclude_unset=True):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No fields provided for update"
            )

        # project_to_update = Project(**updated_details.model_dump())
        updated_project = self.repo.update(
            project_id,
            updated_details.model_dump(exclude_unset=True)
        )

        if not updated_project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found"
            )

        return ProjectResponse.model_validate(updated_project)


    def delete(self, project_id: UUID):
        deleted_project = self.repo.delete(project_id)

        if not deleted_project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project Not found"
            )

        return ProjectResponse.model_validate(deleted_project)


# converting model into schema for better database practices
# def project_to_schema(project: Project):
#     project_response = ProjectResponse()
#
#     project_response.id = project.id
#     project_response.name = project.name
#     project_response.description = project.description
#     project_response.created_at = project.created_at
#
#     return project_response

