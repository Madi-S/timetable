from typing import Never

from app.models.schemas import NotePostPayloadSchema, NotePutPayloadSchema
from app.models.tortoise import Note


async def post(payload: NotePostPayloadSchema) -> int:
    """Returns created note id"""
    # TODO: check and test if user with such id exists,
    # and only then create note
    notes = Note(**payload)
    await notes.save()
    return notes.id


async def get(id: int) -> dict | None:
    """Returns note by id or `None` if not found"""
    if note := await Note.filter(id=id).first().values():
        return note


async def get_all() -> list[dict] | list[Never]:
    """Returns a list of all notes"""
    notes = await Note.all().values()
    return notes


async def delete(id: int) -> int | None:
    """Returns deleted note id"""
    if note := await Note.filter(id=id).first():
        await note.delete()
        return note.id


async def put(id: int, payload: NotePutPayloadSchema) -> dict | None:
    """Returns updated note or `None` if not found"""
    if note := await Note.filter(id=id):
        await note.update(**payload)
        updated_note = await Note.filter(id=id).first().values()
        return updated_note
