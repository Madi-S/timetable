from time import sleep
from celery import shared_task
from asgiref.sync import async_to_sync

from app.utils.filler import fill_tortoise_models


@shared_task
def divide(x: int, y: int) -> float:
    sleep(5)
    return x / y


@shared_task
def fill_database_models() -> None:
    async_to_sync(fill_tortoise_models)()
