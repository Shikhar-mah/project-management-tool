from typing import Optional

from uuid import UUID

from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class ProjectResponse(BaseModel):
    id: UUID
    name: str
    description: Optional[str] = None
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)



