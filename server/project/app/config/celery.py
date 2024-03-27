import os
import logging
from functools import lru_cache


log = logging.getLogger('uvicorn')


class Config:
    pass


@lru_cache()
def get_config() -> Config:
    log.info('Loading celery config from the environment')
    return Config()


config = get_config()
