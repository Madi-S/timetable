import uvicorn
from models import User as ModelUser
from schema import User as SchemaUser
from app import app
from db import db
from fastapi import HTTPException

@app.get('/user/{id}', response_model=SchemaUser)
async def get_user(id: int):
    user = await ModelUser.get(id)
    if user:
        return SchemaUser(**user).dict()
    raise HTTPException(404, 'User with given id does not exist')


@app.post('/user/')
async def create_user(user: SchemaUser):
    user_id = await ModelUser.create(**user.dict())
    return {'user_id': user_id}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
