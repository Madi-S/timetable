from app.models.tortoise import User


async def notify_users_of_notes():
    # notify users of incoming notes via email
    users = await User.all()
    print(len(users))


# once a day delete old notes task
