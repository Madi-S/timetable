import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

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


class NotePostIn(BaseModel):
    user_id: int
    title: str
    description: Optional[str]
    datetime_from: datetime.datetime
    datetime_to: datetime.datetime
    color: enums.NoteColor
    category: enums.NoteCategory


class NotePutIn(BaseModel):
    title: Optional[str]
    description: Optional[str]
    datetime_from: Optional[datetime.datetime]
    datetime_to: Optional[datetime.datetime]
    color: Optional[enums.NoteColor]
    category: Optional[enums.NoteCategory]


class NoteOut(NotePostIn):
    created_at: datetime.datetime

    class Config:
        orm_mode = True
