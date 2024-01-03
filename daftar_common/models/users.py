import datetime
import uuid
from typing import List, Optional

from pydantic import BaseModel, EmailStr


class UserClassroom(BaseModel):
    id_classroom: uuid.UUID
    role: str


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

    def belongs_to_classroom(self, classroom_id: str):
        """
        Returns True if the user belongs to the input classroom_id. False otherwise
        """
        return any(
            map(
                lambda classroom: str(classroom.id_classroom) == classroom_id,
                self.classrooms,
            )
        )

    def update_classroom_role(self, classroom_id: str, role: str):
        """
        If user does not belong to the specified classroom, we create the link.
        Otherwise, we only update its role

        Returns: None
        """
        user_belongs_to_classroom = self.belongs_to_classroom(classroom_id)
        if user_belongs_to_classroom:
            for classroom in self.classrooms:
                if str(classroom.id_classroom) == classroom_id:
                    classroom.role = role
                    break
        else:
            self.classrooms.append(
                UserClassroom(**{"id_classroom": classroom_id, "role": role})
            )

        return

    def deregister_user_from_classroom(self, classroom_id: str):
        """
        Deregister the user from the given classroom_id.
        If the user does not belong to the classroom_id, nothing happens
        Returns: None
        """
        self.classrooms[:] = [
            classroom
            for classroom in self.classrooms
            if str(classroom.id_classroom) != classroom_id
        ]


class Users(BaseModel):
    users: List[User]
