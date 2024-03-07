import os
import logging
from functools import lru_cache
from pydantic import AnyUrl
from pydantic_settings import BaseSettings

log = logging.getLogger('uvicorn')


class Settings(BaseSettings):
    environment: str = os.getenv('ENVIRONMENT', 'dev')  # dev/stage/prod
    testing: bool = os.getenv('TESTING', 0)  # testing mode
    database_url: AnyUrl = os.environ.get('DATABASE_URL')  # db url


@lru_cache()
def get_settings() -> BaseSettings:
    log.info('Loading config settings from the environment')
    return Settings()
