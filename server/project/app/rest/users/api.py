from fastapi import APIRouter, Path, HTTPException, status

from app.rest.users import crud
from app.rest.users import schemas


router = APIRouter()


@router.get('/{id}', status_code=status.HTTP_200_OK)
async def get_user(id: int = Path(..., gt=0)) -> schemas.UserOut:
    if user := await crud.get(id):
        return user
    raise HTTPException(
        status.HTTP_404_NOT_FOUND,
        'User with such id was not found'
    )


# TODO: make sure this route depends on auth only for admins
@router.get('/', status_code=status.HTTP_200_OK)
async def get_all_users() -> list[schemas.UserOut]:
    if users := await crud.get_all():
        return users
    raise HTTPException(
        status.HTTP_404_NOT_FOUND,
        'There are no entries for User'
    )


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(payload: schemas.UserPostIn) -> int:
    if user_id := await crud.post(payload):
        return user_id
    raise HTTPException(
        status.HTTP_409_CONFLICT,
        f'User with such email or username already exists'
    )


@router.put('/{id}', status_code=status.HTTP_200_OK)
async def update_user(payload: schemas.UserPutIn, id: int = Path(..., gt=0)) -> schemas.UserOut:
    if user := await crud.put(id, payload):
        return user
    raise HTTPException(
        status.HTTP_404_NOT_FOUND,
        'User with such id was not found and hence cannot be updated or \
        provided email or username are already taken by another user'.replace('        ', '')
    )


@router.delete('/{id}', status_code=status.HTTP_200_OK)
async def delete_user(id: int = Path(..., gt=0)) -> int:
    if user_id := await crud.delete(id):
        return user_id
    raise HTTPException(
        status.HTTP_404_NOT_FOUND,
        'User with such id was not found and hence cannot be deleted'
    )
