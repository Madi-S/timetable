from typing import Never

from app.api.rest.notes import schemas
from app.models.tortoise import User, Note


async def get(id: int) -> schemas.NoteOut | None:
    """Returns note by id or `None` if not found"""
    return await Note.filter(id=id).first().values()


async def get_all() -> list[schemas.NoteOut] | list[Never]:
    """Returns a list of all notes or an empty list`"""
    return await Note.all().values()


async def get_all_for_user(user_id: int) -> list[schemas.NoteOut] | list[Never]:
    """Returns a list of all notes for a particular user or an empty list"""
    return await Note.filter(user_id=user_id).all().values()


async def post(payload: schemas.NotePostIn) -> int | None:
    """Returns created note id or `None` if user_id not found"""
    if await User.filter(id=payload.user_id).first():
        note = Note(**payload.model_dump())
        await note.save()
        return note.id


async def put(id: int, payload: schemas.NotePutIn) -> schemas.NoteOut | None:
    """Returns updated note or `None` if not found"""
    if await Note.filter(id=id).update(**payload.model_dump()):
        return await Note.filter(id=id).first().values()


async def delete(id: int) -> int | None:
    """Returns deleted note id or `None` if not found"""
    if note := await Note.filter(id=id).first():
        await note.delete()
        return note.id
