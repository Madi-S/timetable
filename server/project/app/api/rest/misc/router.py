from fastapi import APIRouter, Depends

from app.scheduler import scheduler
from app.utils.filler import fill_models
from app.config import Config, get_config


router = APIRouter()


@router.get('/ping')
async def pong(config: Config = Depends(get_config)):
    return {
        'ping': 'pong',
        'testing': config.TESTING,
        'environment': config.ENVIRONMENT
    }


@router.post('/filler')
async def filler():
    # TODO: Use celery here
    await fill_models()
