import os
import logging
from functools import lru_cache


log = logging.getLogger('uvicorn')


class Config:
    TESTING: bool = os.getenv('TESTING', 0)
    ENVIRONMENT: str = os.getenv('ENVIRONMENT', 'dev')
    DATABASE_URL: str = os.environ.get('DATABASE_URL')
    DATABASE_TEST_URL: str = os.environ.get('DATABASE_TEST_URL')
    REDIS_URL = os.environ.get('REDIS_URL', 'redis://127.0.0.1:6379/0')

    SCOUT_USE: bool = os.getenv('SCOUT_USE', False)
    SCOUT_KEY: str = os.getenv('SCOUT_KEY', '******')
    SCOUT_NAME: str = os.getenv('SCOUT_NAME', 'Timetable Scout')
    SCOUT_MONITOR: bool = os.getenv('SCOUT_MONITOR', True)

    RESULT_BACKEND: str = os.environ.get('RESULT_BACKEND', REDIS_URL)
    CELERY_BROKER_URL: str = os.environ.get('CELERY_BROKER_URL', REDIS_URL)


@lru_cache()
def get_config() -> Config:
    log.info('Loading config from the environment')
    return Config()


config = get_config()
