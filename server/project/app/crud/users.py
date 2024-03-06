from typing import Never

from app.models.schemas import UserPostPayloadSchema, UserPutPayloadSchema
from app.models.tortoise import User


async def post(payload: UserPostPayloadSchema) -> int:
    """Returns created user id"""
    # TODO: check if user with such email or username already exists
    # TODO: add token field to db user
    user = User(**payload)
    await user.save()
    return user.id


async def get(id: int) -> dict | None:
    """Returns user by id or `None` if not found"""
    if user := await User.filter(id=id).first().values():
        return user


async def get_all() -> list[dict] | list[Never]:
    """Returns a list of all users"""
    users = await User.all().values()
    return users


async def delete(id: int) -> int | None:
    """Returns deleted user id"""
    # TODO: check if user does not exist
    if user := await User.filter(id=id).first():
        # return await user.delete()
        return user.id


async def put(id: int, payload: UserPutPayloadSchema) -> dict | None:
    """Returns updated user or `None` if not found"""
    if user := await User.filter(id=id):
        await user.update(**payload)
        updated_user = await User.filter(id=id).first().values()
        return updated_user
