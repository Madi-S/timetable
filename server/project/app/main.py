import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api import ping, users, notes
from app.db import init_db


log = logging.getLogger('uvicorn')


def create_application() -> FastAPI:
    application = FastAPI(lifespan=lifespan)
    application.include_router(ping.router, tags=['ping'])
    application.include_router(
        users.router, prefix='/users', tags=['users']
    )
    application.include_router(
        notes.router, prefix='/notes', tags=['notes']
    )

    return application


@asynccontextmanager
async def lifespan(app: FastAPI):
    log.info('Starting up ...')
    init_db(app)
    yield
    log.info('Shutting down ...')


app = create_application()
