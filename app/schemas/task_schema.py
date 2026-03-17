from typing import Optional
from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.utils.enums import Status, Priority


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Priority
    project_id: UUID
    assignee_id: UUID

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[Status] = None
    priority: Optional[Priority] = None
    assignee_id: Optional[UUID] = None

class TaskResponse(BaseModel):
    id: UUID
    title: str
    description: Optional[str] = None
    status: Status
    priority: Priority
    project_id: UUID
    # project_name: str
    assignee_id: UUID
    # assignee_name: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)