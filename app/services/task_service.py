from typing import Optional
from uuid import UUID

from fastapi import HTTPException, status

from app.models.task import Task
from app.repositories.project_repository import ProjectRepository
from app.repositories.task_repository import TaskRepository
from app.repositories.user_repository import UserRepository
from app.schemas.task_schema import TaskCreate, TaskUpdate, TaskResponse
from app.services.ai_service import generate_description, suggest_priority
from app.utils.enums import Status


class TaskService:
    def __init__(self, repo: TaskRepository, repo_project: ProjectRepository, repo_user: UserRepository):
        self.repo = repo
        self.repo_project = repo_project
        self.repo_user = repo_user

    def create_task(self, task: TaskCreate):
        # new_task = Task(**task.model_dump())

        #check if project exists
        project = self.repo_project.get_by_id(task.project_id)
        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found"
            )

        #check if user exists
        user = self.repo_user.get_by_id(task.assignee_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        # if both of them passes, then add the task
        new_task = Task(**task.model_dump(), status=Status.todo)
        return TaskResponse.model_validate(self.repo.create(new_task))

    def get_by_id(self, task_id: UUID):
        task = self.repo.get_by_id(task_id)

        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        return TaskResponse.model_validate(task)

    def get_all(self):
        return [
            TaskResponse.model_validate(t) for t in self.repo.get_all()
        ]

    def update(self, task_id: UUID, updated_details: TaskUpdate):
        # check if project exists
        task = self.repo.get_by_id(task_id)
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not present"
            )

        # if task present
        updated_task = self.repo.update(
            task_id,
            updated_details.model_dump(exclude_unset=True)
        )

        return TaskResponse.model_validate(updated_task)

    def delete(self, task_id: UUID):
        deleted_task = self.repo.delete(task_id)

        if not deleted_task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task Not found"
            )

        return TaskResponse.model_validate(deleted_task)

    """
    Create a service that would assign the function with a description, 
    and assign it with a priority
    Steps to do it:
    1. Fetch the task by task id
    2. get the title
    3. Generate the description from that title
    4. it's better to create a function specifically for the task of updating the
        the description
    """
    def description_generator_priority(self, task_id: UUID):
        task = self.get_by_id(task_id)
        task_update = TaskUpdate.model_validate(task)
        task_update.description = generate_description(task_update.title)
        task_update.priority = suggest_priority(task_update.title, task_update.description)

        self.update(task_id, task_update)



    # for changing model to schema for better databases practices
    # def task_to_schema(self, task: Task):
    #     task_response = TaskResponse()
    #
    #     task_response.id = task.id
    #     task_response.title =task.title
    #     task_response.description = task.description
    #     task_response.status = task.status
    #     task_response.priority = task.priority
    #     task_response.project_id = task.project_id
    #     # task_response.project_name = self.repo_project.get_by_id(
    #     #     task.project_id).name
    #     task_response.assignee_id = task.assignee_id
    #     # task_response.assignee_name = self.repo_user.get_by_id(
    #     #     task.assignee_id).name
    #     task_response.created_at = task.created_at
    #
    #     return task_response