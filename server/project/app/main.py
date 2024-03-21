import logging
from fastapi import FastAPI

from app.db import init_db
from app.config import get_config
from app.scheduler import register_tasks, unregister_tasks
from app.rest import misc_router, users_router, notes_router


log = logging.getLogger('uvicorn')


def create_application() -> FastAPI:
    def app_on_startup():
        log.info('Starting up ...')
        register_tasks()
        log.info('Scheduler intialized and tasks registered')
        init_db(app)
        log.info('Database intialized')

    def app_on_shutdown():
        log.info('Shutting down ...')
        unregister_tasks()
        log.info('Scheduler shutdown and tasks unregistered')

    application = FastAPI(
        version='0.1.0',
        title='Timetable',
        root_path='/api/v1',
        openapi_url='/api/v1/openapi.json',
        terms_of_service='http://example.com/terms/'
    )

    config = get_config()
    if config.SCOUT_USE:
        from scout_apm.api import Config as ScoutConfig
        from scout_apm.async_.starlette import ScoutMiddleware
        ScoutConfig.set(
            key=config.SCOUT_KEY,
            name=config.SCOUT_NAME,
            monitor=config.SCOUT_MONITOR
        )
        app.add_middleware(ScoutMiddleware)

    application.add_event_handler('startup', app_on_startup)
    application.add_event_handler('shutdown', app_on_shutdown)
    application.include_router(
        tags=['misc'],
        prefix='/rest/misc',
        router=misc_router
    )
    application.include_router(
        tags=['users'],
        prefix='/rest/users',
        router=users_router
    )
    application.include_router(
        tags=['notes'],
        prefix='/rest/notes',
        router=notes_router
    )
    return application


app = create_application()
