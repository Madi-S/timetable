from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.tasks.test import test
from app.tasks.notifier import celery_task_send_email, remove_outdated_notes


scheduler = AsyncIOScheduler()


def register_tasks():
    scheduler.add_job(id='test', func=test, trigger='seconds', seconds=5)
    scheduler.add_job(id='notifer', func=notifier.notify_users_of_notes, trigger='minutes', seconds=15)
