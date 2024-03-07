from typing import Never

from app.utils.secret import Secret
from app.models.tortoise import User
from app.models import schemas


async def post(payload: schemas.UserPostIn) -> int | None:
    """Returns created user id"""
    if user := await User.filter(email=payload.email).first():
        return None
    if user := await User.filter(username=payload.username).first():
        return None

    dump = {}
    dump['token'] = Secret.token
    dump['password_hash'] = str(await Secret.generate_password_hash(payload.password))
    dump.update(payload.model_dump(exclude='password'))

    user = User(**dump)
    await user.save()
    return user.id


async def get(id: int) -> schemas.UserOut | None:
    """Returns user by id or `None` if not found"""
    if user := await User.filter(id=id).first().values():
        return user


async def get_all() -> list[schemas.UserOut] | list[Never]:
    """Returns a list of all users"""
    users = await User.all().values()
    return users


async def delete(id: int) -> int | None:
    """Returns deleted user id"""
    if user := await User.filter(id=id).first():
        await user.delete()
        return user.id


async def put(id: int, payload: schemas.UserPutIn) -> schemas.UserOut | None:
    """Returns updated user or `None` if not found"""
    if user := await User.filter(id=id):
        await user.update(**payload)
        updated_user = await User.filter(id=id).first().values()
        return updated_user
