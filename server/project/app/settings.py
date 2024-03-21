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


@lru_cache()
def get_settings() -> Settings:
    log.info('Loading pydantic base settings from the environment')
    return Settings()
