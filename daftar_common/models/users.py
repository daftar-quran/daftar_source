import datetime
import uuid
from typing import List, Optional

from pydantic import BaseModel, EmailStr


class UserClassroom(BaseModel):
    id_classroom: uuid.UUID
    is_teacher: str


class User(BaseModel, validate_assignment=True):
    id: Optional[uuid.UUID] = None
    pseudo: str
    firstname: str
    lastname: str
    email: EmailStr
    _is_admin: bool = False
    birthdate: datetime.date
    address: Optional[str] = ""
    classrooms: List[UserClassroom] = []
    created_at: Optional[datetime.datetime] = datetime.datetime.now()
    phone_number: Optional[str] = None

    @property
    def is_admin(self) -> bool:
        return self._is_admin


class Users(BaseModel):
    users: List[User]
