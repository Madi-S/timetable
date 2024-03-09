import json
import pytest
import random

from app.models.tortoise import User


async def test_create_user(test_app_with_db):
    id_ = random.randint(1000, 10000000)
    payload = json.dumps({
        'email': f'email.{id_}@gmail.com',
        'password': f'some-password-{id_}',
        'username': f'some unique username {id_}',
    })

    response = test_app.post('/users/', data=payload)

    assert response.status_code == 201
    assert response.json()['id'] is not None
    assert (await User.filter(email=payload['email']).first())
