import logging
from fastapi import FastAPI

from app.db import init_db
from app.api import ping, users, notes


log = logging.getLogger('uvicorn')


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router, tags=['ping'])
    application.include_router(
        users.router, prefix='/users', tags=['users']
    )
    application.include_router(
        notes.router, prefix='/notes', tags=['notes']
    )

    return application


app = create_application()


@app.on_event('startup')
async def startup_event():
    log.info('Starting up ...')
    init_db(app)
    log.info('Database intialized')


@app.on_event('shutdown')
def shutdown_event():
    log.info('Shutting down ...')
