from typing import Optional
from pydantic import BaseModel, EmailStr
from tortoise.contrib.pydantic import pydantic_model_creator

from app.models.tortoise import User, Note
from app.models import enums


# TODO: add camelCaseModel
# TODO: add validators


class UserPostIn(BaseModel):
    username: str
    password: str
    email: EmailStr


class UserPutIn(BaseModel):
    email: Optional[EmailStr]
    username: Optional[str]

    # TODO: add validator that at least one field is not `None`


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True


class NoteBaseModel(BaseModel):
    user_id: int


class NotePostIn(NoteBaseModel):
    title: str
    description: Optional[str]
    datetime_from: str
    datetime_to: str
    color: enums.NoteColor
    category: enums.NoteCategory


class NotePutIn(NoteBaseModel):
    title: Optional[str]
    description: Optional[str]
    datetime_from: Optional[str]
    datetime_to: Optional[str]
    color: Optional[enums.NoteColor]
    category: Optional[enums.NoteCategory]


class NoteOut(NotePostIn):

    class Config:
        orm_mode = True
