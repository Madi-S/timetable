from fastapi import APIRouter

from app.api.rest.misc.router import router as misc_router
from app.api.rest.users.router import router as users_router
from app.api.rest.notes.router import router as notes_router


router = APIRouter()
router.include_router(
    tags=['misc'],
    prefix='/misc',
    router=misc_router
)
router.include_router(
    tags=['users'],
    prefix='/users',
    router=users_router
)
router.include_router(
    tags=['notes'],
    prefix='/notes',
    router=notes_router
)
