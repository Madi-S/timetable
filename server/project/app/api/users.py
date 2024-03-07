from fastapi import APIRouter, Path, HTTPException, status

from app.crud import users as crud
from app.models import schemas


router = APIRouter()


@router.post('/', response_model=int, status_code=status.HTTP_201_CREATED)
async def create_user(payload: schemas.UserPostIn):
    if user_id := await crud.post(payload):
        return user_id
    raise HTTPException(
        status.HTTP_409_CONFLICT,
        f'User with such email or username already exists'
    )


@router.get('/{id}', response_model=schemas.UserOut, status_code=status.HTTP_200_OK)
async def get_user(id: int = Path(..., gt=0)):
    if user := await crud.get(id):
        return user
    raise HTTPException(
        status.HTTP_404_NOT_FOUND,
        'User with such id is not found'
    )


# TODO: make sure this route depends on auth only for admins
@router.get('/', response_model=list[schemas.UserOut])
async def get_all_users():
    if users := await crud.get_all():
        return users


@router.put('/{id}', response_model=schemas.UserOut, status_code=status.HTTP_200_OK)
async def update_user(payload: schemas.UserPutIn, id: int = Path(..., gt=0)):
    pass
