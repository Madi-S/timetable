from app.models.tortoise import User


async def notify_users_of_notes():
    # TODO: implement celery with flower to notify users of incoming notes via email
    users = await User.all.only(User.id, User.email)
    for user in users:
        celery_task_send_email(user.email)


async def remove_outdated_notes():
    pass


def celery_task_send_email(email: str):
    print(f'Sending email to {email}')
