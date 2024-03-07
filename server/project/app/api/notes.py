from fastapi import APIRouter, Path, HTTPException, status

from app.models import schemas
from app.crud import notes as crud


router = APIRouter()


@router.get('/{id}', status_code=status.HTTP_200_OK)
async def get_note(id: int = Path(..., gt=0)) -> schemas.NoteOut:
    if note := await crud.get(id):
        return note
    raise HTTPException(
        status.HTTP_404_NOT_FOUND,
        'Note with such id was not found'
    )


@router.get('/', status_code=status.HTTP_200_OK)
async def get_all_notes() -> list[schemas.NoteOut]:
    if notes := await crud.get_all():
        return notes
    raise HTTPException(
        status.HTTP_404_NOT_FOUND,
        'There are no entries for Note'
    )


@router.get('/user/{user_id}', status_code=status.HTTP_200_OK)
async def get_all_notes_for_user(user_id: int = Path(..., gt=0)) -> list[schemas.NoteOut]:
    if notes := await crud.get_all_for_user(user_id):
        return notes
    raise HTTPException(
        status.HTTP_404_NOT_FOUND,
        'No notes were found for this user'
    )


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_note(payload: schemas.NotePostIn) -> int:
    if note_id := await crud.post(payload):
        return note_id
    raise HTTPException(
        status.HTTP_404_NOT_FOUND,
        'Cannot create note, probably user with given id was not found'
    )


@router.put('/{id}', status_code=status.HTTP_200_OK)
async def update_note(payload: schemas.NotePutIn, id: int = Path(..., gt=0)) -> schemas.NoteOut:
    if note := await crud.put(id, payload):
        return note
    raise HTTPException(
        status.HTTP_404_NOT_FOUND,
        'Note with such id is not found and hence cannot be updated'
    )


@router.delete('/{id}', status_code=status.HTTP_200_OK)
async def delete_note(id: int = Path(..., gt=0)) -> int:
    if note_id := await crud.delete(id):
        return note_id
    raise HTTPException(
        status.HTTP_404_NOT_FOUND,
        'Note with such id is not found and hence cannot be deleted'
    )
