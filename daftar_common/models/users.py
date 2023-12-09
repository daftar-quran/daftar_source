import datetime
import uuid
from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field


class UserClassroom(BaseModel):
    id_classroom: uuid.UUID
    is_teacher: str


class User(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    pseudo: str
    firstname: str
    lastname: str
    email: EmailStr
    is_admin: bool
    birthdate: datetime.date
    address: Optional[str] = ""
    classrooms: List[UserClassroom] = []
    created_at: Optional[datetime.datetime] = datetime.datetime.now()
