# from sqlmodel import SQLModel
from dataclasses import Field
from typing import Optional

from sqlmodel import SQLModel

import app.db


class Project(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

from sqlmodel import create_engine
