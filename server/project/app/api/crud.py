from app.models.models import (
    Note,
    User,
    NoteSchema,
    UserSchema,
    NoteInSchema,
    UserInSchema
)


async def post_user(payload: UserInSchema) -> int:
    """Returns created user id"""
    user = User(email=UserInSchema.email)
    await user.save()
    return user.id


async def get_all_users() -> list[dict]:
    """Returns all users"""
    users = await User.all().values()
    return users


async def get_user(id: int) -> dict | None:
    """Returns user `dict` by id or `None` if not found"""
    if user := await User.filter(id=id).first().values():
        return user


async def delete_user(id: int) -> int:
    """Returns deleted user id"""
    user = await User.filter(id=id).first().delete()
    return user


async def put_user(id: int, payload: UserInSchema) -> dict | None:
    """Returns updated user `dict` or `None` if not found"""
    if await User.filter(id=id).update(email=payload.email):
        updated_user = await User.filter(id=id).first().values()
        return updated_user


async def post_note(user_id: int, payload: NoteInSchema) -> int:
    """Returns created note id"""
    if user := await User.filter(id=user_id).first(): 
        note = Note(title=payload.title, color=payload.color, description=payload.description, date=payload.datetime, user=user)
        await note.save()
        return note.id


async def delete_note(id: int):
    """Returns deleted note id"""
    note = await Note.filter(id=id).first().delete()
    return note


async def pute_note(id: int, payload: NoteInSchema):
    """Returns updated post `dict` or `None` if not found"""
    if await Note.filter(id=id).update(**payload):
        updated_note = await Note.filter(id=id).first().values()
        return updated_note


async def get_note(id: int):
    """Returns note `dict` by id or `None` if not found"""
    if note := await Note.filter(id=id).first().values():
        return note


async def get_all_notes():
    """Returns all notes"""
    notes = await Note.all().values()
    return notes


async def get_all_notes_by_user_id(user_id: int) -> list[Note] | None:
    """Returns all notes by user_id"""
    if user := await User.filter(user_id=user_id).first():
        notes = await Note.filter(user=user).all().values()
        return notes