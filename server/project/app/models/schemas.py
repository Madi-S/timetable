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
    # TODO: test it and maybe use `Optional`
    email: EmailStr | None = None
    password: str | None = None
    username: str | None = None


class NotePostSchema(BaseModel):
    user_id: int
    title: str
    description: str | None = None
    datetime_from: str
    datetime_to: str
    color: enums.NoteColor
    category: enums.NoteCategory


UserOutSchema = pydantic_model_creator(User, exclude=('password_hash'))
NoteOutSchema = pydantic_model_creator(Note, exclude=('edited_at'))
