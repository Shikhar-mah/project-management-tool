import uuid
from datetime import datetime

from sqlalchemy import Column, String, Text, ForeignKey, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID

from app.db import Base
from app.utils.enums import Status, Priority


class Task(Base):
    __tablename__ = "tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    status = Column(Enum(Status), nullable=False, default=Status.todo)
    priority = Column(Enum(Priority), nullable=True)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"))
    assignee_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)