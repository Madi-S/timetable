from typing import Optional
from pydantic import BaseModel, EmailStr


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
        from_attributes = True
