from pydantic import BaseModel

import enums


class User(BaseModel):
    id: str


class Note(BaseModel):
    title: str
    user_id: str
    datetime: str
    description: str
    color: enums.Color

    class Config:
        use_enum_values = True
