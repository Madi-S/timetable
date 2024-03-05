from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from app.models.tortoise import User, Note
from app.models import enums


# TODO: add camelCaseModel


class UserInSchema(BaseModel):
    email: str
    password: str
    username: str


class NoteInSchema(BaseModel):
    user_id: int
    title: str
    description: str | None = None
    datetime_from: str
    datetime_to: str
    color: enums.NoteColor
    category: enums.NoteCategory


UserOutSchema = pydantic_model_creator(User, exclude=('password_hash'))
NoteOutSchema = pydantic_model_creator(Note, exclude=('edited_at'))
