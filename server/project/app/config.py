import os
import logging
from functools import lru_cache


log = logging.getLogger('uvicorn')


class Config:
    SCOUT_USE: bool = os.getenv('SCOUT_USE', False)
    SCOUT_KEY: str = os.getenv('SCOUT_KEY', '******')
    SCOUT_NAME: str = os.getenv('SCOUT_NAME', 'Timetable Scout')
    SCOUT_MONITOR: bool = os.getenv('SCOUT_MONITOR', True)


@lru_cache()
def get_config() -> Config:
    log.info('Loading config from the environment')
    return Config()
