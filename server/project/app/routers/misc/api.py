from fastapi import APIRouter, Depends

from app.scheduler import scheduler
from app.utils.filler import fill_models
from app.settings import Settings, get_settings

router = APIRouter()


@router.get('/ping')
async def pong(settings: Settings = Depends(get_settings)):
    return {
        'ping': 'pong',
        'testing': settings.TESTING,
        'environment': settings.ENVIRONMENT
    }


@router.post('/filler')
async def filler():
    # TODO: Use celery here
    await fill_models()
