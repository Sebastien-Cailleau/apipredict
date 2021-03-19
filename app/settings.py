from functools import lru_cache

import config


@lru_cache()
def get_settings():
    """
    get .env constant
    """
    return config.Settings()


settings = get_settings()
