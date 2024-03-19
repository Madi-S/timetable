import logging
from fastapi import FastAPI

from app.db import init_db
from app.scheduler import scheduler, register_tasks
from app.routers.misc.api import router as misc_router
from app.routers.users.api import router as users_router
from app.routers.notes.api import router as notes_router


log = logging.getLogger('uvicorn')


def create_application() -> FastAPI:
    application = FastAPI(
        version='1.0',
        title='Timetable Server'
    )
    application.add_event_handler('startup', app_on_startup)
    application.add_event_handler('shutdown', app_on_shutdown)
    application.include_router(
        tags=['misc'],
        prefix='/api/misc',
        router=misc_router
    )
    application.include_router(
        tags=['users'],
        prefix='/api/users',
        router=users_router
    )
    application.include_router(
        tags=['notes'],
        prefix='/api/notes',
        router=notes_router
    )
    return application


app = create_application()


async def app_on_startup():
    log.info('Starting up ...')
    register_tasks()
    scheduler.start()
    init_db(app)
    log.info('Database intialized')


def app_on_shutdown():
    log.info('Shutting down ...')
    scheduler.shutdown(wait=False)
