import logging
from fastapi import FastAPI, Depends

from app.db import init_db
from app.utils.filler import fill_models
from app.config import Settings, get_settings
from app.users.api import router as users_router
from app.notes.api import router as notes_router


log = logging.getLogger('uvicorn')


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(users_router, prefix='/users', tags=['users'])
    application.include_router(notes_router, prefix='/notes', tags=['notes'])
    return application


app = create_application()


@app.get('/ping')
async def pong(settings: Settings = Depends(get_settings)):
    return {
        'ping': 'pong',
        'environment': settings.environment,
        'testing': settings.testing,
    }


@app.post('/filler')
async def filler():
    await fill_models()


@app.on_event('startup')
async def startup_event():
    log.info('Starting up ...')
    init_db(app)
    log.info('Database intialized')


@app.on_event('shutdown')
def shutdown_event():
    log.info('Shutting down ...')
