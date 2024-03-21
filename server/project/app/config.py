import os
import logging
from functools import lru_cache
from pydantic import AnyUrl
from pydantic_settings import BaseSettings


log = logging.getLogger('uvicorn')


class Settings(BaseSettings):
    TESTING: bool = os.getenv('TESTING', 0)

    ENVIRONMENT: str = os.getenv('ENVIRONMENT', 'dev')

    DATABASE_URL: AnyUrl = os.environ.get('DATABASE_URL')

    SCOUT_USE = os.getenv('SCOUT_USE', False)
    SCOUT_KEY = os.getenv('SCOUT_KEY', '******')
    SCOUT_NAME = os.getenv('SCOUT_NAME', 'Timetable Scout')
    SCOUT_MONITOR = os.getenv('SCOUT_MONITOR', True)


@lru_cache()
def get_settings() -> Settings:
    log.info('Loading config settings from the environment')
    return Settings()
