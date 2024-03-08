from fastapi import APIRouter, Depends

from app.utils.filler import fill_models
from app.config import Settings, get_settings


router = APIRouter()


@router.get('/ping')
async def pong(settings: Settings = Depends(get_settings)):
    return {
        'ping': 'pong',
        'environment': settings.environment,
        'testing': settings.testing,
    }


@router.post('/filler')
async def filler():
    await fill_models()
