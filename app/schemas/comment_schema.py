from typing import Optional

from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime

class CommentCreate(BaseModel):
    task_id: UUID
    user_id: UUID
    comment: str

class CommentResponse(BaseModel):
    id: UUID
    user_id: UUID
    task_id: UUID
    comment: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
