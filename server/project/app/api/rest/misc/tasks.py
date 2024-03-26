import asyncio
from time import sleep
from celery import shared_task

from app.db import connect_db, disconnect_db
from app.utils.filler import fill_tortoise_models


async def wrap_db_ctx(func, *args, **kwargs) -> None:
    """
    Allows running async function in sync way with tortoise database context
    Usage: `asyncio.run(wrap_db_ctx(create_some_user, name='Alex', age=25))`
    """
    try:
        await connect_db()
        await func(*args, **kwargs)
    finally:
        await disconnect_db()


@shared_task
def divide(x: int, y: int) -> float:
    """Sample task for division to make sure celery worker is up and running"""
    sleep(5)
    return x / y


@shared_task
def fill_database_models() -> None:
    """Fills out the database models with random data"""
    # TODO: add transaction here
    asyncio.run(wrap_db_ctx(fill_tortoise_models))
