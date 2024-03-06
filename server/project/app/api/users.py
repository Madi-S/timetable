from fastapi import APIRouter, Path

from app.crud import users as crud
from app.models.schemas import UserPostPayloadSchema, UserPutPayloadSchema, UserOutSchema


router = APIRouter()


@router.post('/', response_model=int)
async def create_user(payload: UserPostPayloadSchema):
    print('!!!', payload)
    user_id = await crud.post(payload)
    return user_id


@router.get('/{id}/', response_model=UserOutSchema)
async def get_user(user_id: int = Path(..., gt=0)):
    user = await crud.get(user_id)
    return user


# TODO: make sure this route depends on auth only for admins
@router.get('/', response_model=list[UserOutSchema])
async def get_all_users():
    users = await crud.get_all()
    return users
