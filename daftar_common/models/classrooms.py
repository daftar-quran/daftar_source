import datetime
import uuid
from typing import List, Optional
from pydantic import BaseModel


class AdminId(BaseModel):
    id_classroom: uuid.UUID


class PermanentTeacherId(BaseModel):
    id_classroom: uuid.UUID


class TemporaryTeacherId(BaseModel):
    id_classroom: uuid.UUID


class StudentId(BaseModel):
    id_classroom: uuid.UUID


class CourseDescription(BaseModel):
    id: uuid.UUID
    date: datetime.datetime


class Classroom(BaseModel):
    id: Optional[uuid.UUID] = None
    name: str
    tikrar_goal: str
    admins: List[AdminId]
    permanent_teachers: List[PermanentTeacherId]
    temporary_teachers: List[TemporaryTeacherId]
    students: List[StudentId]
    courses: List[CourseDescription]
