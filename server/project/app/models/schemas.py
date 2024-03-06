from typing import Optional
from pydantic import BaseModel, EmailStr
from tortoise.contrib.pydantic import pydantic_model_creator

from app.models.tortoise import User, Note
from app.models import enums


# TODO: add camelCaseModel
# TODO: add validators


class UserPostPayloadSchema(BaseModel):
    email: EmailStr
    password: str
    username: str


class UserPutPayloadSchema(BaseModel):
    email: Optional[EmailStr]
    password: Optional[str]
    username: Optional[str]

    # TODO: add validator that at least one field is not `None`


class NoteBaseModel(BaseModel):
    user_id: int


class NotePostPayloadSchema(NoteBaseModel):
    title: str
    description: Optional[str]
    datetime_from: str
    datetime_to: str
    color: enums.NoteColor
    category: enums.NoteCategory


class NotePutPayloadSchema(NoteBaseModel):
    title: Optional[str]
    description: Optional[str]
    datetime_from: Optional[str]
    datetime_to: Optional[str]
    color: Optional[enums.NoteColor]
    category: Optional[enums.NoteCategory]


UserOutSchema = pydantic_model_creator(User, exclude=('password_hash'))
NoteOutSchema = pydantic_model_creator(Note, exclude=('edited_at'))
