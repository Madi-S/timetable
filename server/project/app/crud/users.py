from typing import Never

from app.models import schemas
from app.utils.secret import Secret
from app.models.tortoise import User


async def get(id: int) -> schemas.UserOut | None:
    """Returns user by id or `None` if not found"""
    return await User.filter(id=id).first().values()


async def get_all() -> list[schemas.UserOut] | list[Never]:
    """Returns a list of all users or an empty list"""
    return await User.all().values()


async def post(payload: schemas.UserPostIn) -> int | None:
    """Returns created user id or `None` if email or username is already taken"""
    if not (await User.filter(email=payload.email) or await User.filter(username=payload.username)):
        dump = {}
        dump['token'] = Secret.token
        dump['password_hash'] = str(await Secret.generate_password_hash(payload.password))
        dump.update(payload.model_dump(exclude='password'))
        user = User(**dump)
        await user.save()
        return user.id


async def put(id: int, payload: schemas.UserPutIn) -> schemas.UserOut | None:
    """Returns updated user or `None` if not found"""
    # TODO: make sure to check if user wants to update username or email
    # which are already taken by another user
    # catch `tortoise.exceptions.IntegrityError` exception in that case?
    if await User.filter(id=id).first().update(**payload.model_dump()):
        return await User.filter(id=id).first().values()


async def delete(id: int) -> int | None:
    """Returns deleted user id or `None` if not found"""
    if user := await User.filter(id=id).first():
        await user.delete()
        return user.id
