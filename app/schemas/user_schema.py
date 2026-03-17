from datetime import datetime

from pydantic import BaseModel, EmailStr, ConfigDict
from uuid import UUID


class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)