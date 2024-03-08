import logging
from fastapi import FastAPI
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.db import init_db

from app.tasks import notifier
from app.routers.misc.api import router as misc_router
from app.routers.users.api import router as users_router
from app.routers.notes.api import router as notes_router


log = logging.getLogger('uvicorn')


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(misc_router, prefix='/misc', tags=['misc'])
    application.include_router(users_router, prefix='/users', tags=['users'])
    application.include_router(notes_router, prefix='/notes', tags=['notes'])
    return application


app = create_application()


def job_counter():
    log.info(f'It is regular interval job')


scheduler = AsyncIOScheduler()


@app.on_event('startup')
async def startup_event():
    log.info('Starting up ...')
    # scheduler.add_job(id='job1', func=job_counter, trigger='cron', second='*/2')
    scheduler.add_job(id='notifer', func=notifier.notify_users_of_notes,
                      trigger='minutes', seconds=15)
    scheduler.start()
    init_db(app)
    log.info('Database intialized')


@app.on_event('shutdown')
def shutdown_event():
    log.info('Shutting down ...')
    scheduler.shutdown(wait=False)
