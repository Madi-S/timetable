import random
import asyncio
from faker import Faker

from app.models import enums
from app.utils.secret import Secret
from app.models.tortoise import User, Note


fake = Faker()


async def fill_models():
    user_ids = []
    for _ in range(50):
        password_hash = await Secret.generate_password_hash(
            fake.unique.name()
        )
        user = User(
            email=fake.unique.email(),
            username=fake.unique.user_name(),
            password_hash=password_hash,
            token=Secret.token
        )
        await user.save()
        user_ids.append(user.id)

    for i in range(200):
        color = random.choice(list(enums.NoteColor))
        category = random.choice(list(enums.NoteCategory))
        note = Note(
            user_id=random.choice(user_ids),
            title=f'Title #{i}',
            description=fake.text(),
            datetime_from=fake.date_time(),
            datetime_to=fake.date_time(),
            color=color,
            category=category
        )
        await note.save()


if __name__ == '__main__':
    asyncio.run(fill_models())
