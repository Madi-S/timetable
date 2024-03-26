from fastapi import APIRouter

from app.api.rest.misc import tasks
from app.config import get_config as _get_config
# from app.celery_utils import get_task_info


router = APIRouter()


@router.get('/ping')
async def pong():
    return {'ping': 'pong'}


@router.get('/config')
async def get_config():
    config = _get_config()
    return {
        'TESTING': config.TESTING,
        'REDIS_URL': config.REDIS_URL,
        'SCOUT_USE': config.SCOUT_USE,
        'ENVIRONMENT': config.ENVIRONMENT,
        'DATABASE_URL': config.DATABASE_URL,
        'DATABASE_TEST_URL': config.DATABASE_TEST_URL,
        'CELERY_RESULT_BACKEND': config.RESULT_BACKEND
    }


@router.post('/celery')
async def test_celery_task():
    task = tasks.divide.delay(10, 5)
    return {'task_id': task.task_id}


# @router.get('/celery/{task_id}')
# async def get_celery_task_info(task_id: str):
#     response = get_task_info(task_id)
#     return JSONResponse(response)


# @router.post('/celery/filler')
# async def fill_database_models():
#     task = tasks.fill_database_models.delay()
#     return {'task_id': task.task_id}
