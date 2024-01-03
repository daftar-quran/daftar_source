import datetime
import uuid
from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class ClassroomRoles(Enum):
    admin = "admin"
    temporary_teacher = "temporary_teacher"
    permanent_teacher = "permanent_teacher"
    student = "student"


class CourseDescription(BaseModel):
    id: uuid.UUID
    date: datetime.datetime


class Classroom(BaseModel, validate_assignment=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str
    tikrar_goal: int
    admins: List[uuid.UUID]
    permanent_teachers: List[uuid.UUID] = []
    temporary_teachers: List[uuid.UUID] = []
    students: List[uuid.UUID] = []
    courses: List[CourseDescription] = []

    def get_user_role(self, user_id: str):
        """
        Returns the role of the given user_id in classroom.
        if user_id is not in classroom, returns None
        """
        for adm in self.admins:
            if str(adm) == user_id:
                return ClassroomRoles.admin

        for pt in self.permanent_teachers:
            if str(pt) == user_id:
                return ClassroomRoles.permanent_teacher

        for tt in self.temporary_teachers:
            if str(tt) == user_id:
                return ClassroomRoles.temporary_teacher

        for student in self.students:
            if str(student) == user_id:
                return ClassroomRoles.student
        return None


class Classrooms(BaseModel):
    classrooms: List[Classroom]
