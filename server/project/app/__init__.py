import logging
from fastapi import FastAPI

from app.db import init_db, disconnect_db
from app.config import config
from app.celery_utils import create_celery
from app.api import rest_router, graphql_route, rpc_app


log = logging.getLogger('uvicorn')


def create_app() -> FastAPI:
    async def app_on_startup():
        log.info('Starting up ...')
        init_db(app)
        log.info('Database intialized')

    async def app_on_shutdown():
        log.info('Shutting down ...')
        await disconnect_db()

        log.info('Database connection closed')

    app = FastAPI(
        version='0.1.0',
        title='Timetable',
        root_path='/api/v1',
        terms_of_service='http://example.com/terms',
        description='''
            This documentation presents endpoints description for REST
            \nYou can also view other documentations here:
            \n<a href="/api/v1/jsonrpc/docs"><b>JSON-RPC documentation</b></a>
            \n<a href="/api/v1/graphql"><i>GraphQL</i></a>
        '''.strip()
    )

    # Celery
    app.celery_app = create_celery()

    # Event Handlers / Lifespan
    # TODO: use lifespan
    app.add_event_handler('startup', app_on_startup)
    app.add_event_handler('shutdown', app_on_shutdown)

    # JSON-RPC
    app.mount('/rpc', rpc_app)

    # REST
    app.include_router(rest_router, prefix='/rest')

    # GraphQL
    app.add_route('/graphql', graphql_route)
    app.add_websocket_route('/graphql', graphql_route)

    if config.SCOUT_USE:
        from scout_apm.api import Config as ScoutConfig
        from scout_apm.async_.starlette import ScoutMiddleware
        ScoutConfig.set(
            key=config.SCOUT_KEY,
            name=config.SCOUT_NAME,
            monitor=config.SCOUT_MONITOR
        )
        app.add_middleware(ScoutMiddleware)

    return app


app = create_app()
