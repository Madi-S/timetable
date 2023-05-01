import datetime
from pydantic import BaseModel

import enums


class Note(BaseModel):
    title: str
    user_id: int
    datetime: str
    description: str
    color: enums.Color

    class Config:
        use_enum_values = True


class NoteIn(Note):
    pass


class NoteOut(Note):
    created_at: datetime.datetime
    id: int
