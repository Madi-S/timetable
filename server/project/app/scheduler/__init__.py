from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.scheduler.notifier import notify_users_of_notes, remove_outdated_notes


scheduler = AsyncIOScheduler()


def register_tasks():
    scheduler.add_job(
        id='notifer',
        func=notify_users_of_notes,
        trigger='interval',
        hours=1
    )
    scheduler.add_job(
        id='cleaner',
        func=remove_outdated_notes,
        trigger='interval',
        hours=5
    )
    scheduler.start()


def unregister_tasks():
    scheduler.shutdown(wait=False)
