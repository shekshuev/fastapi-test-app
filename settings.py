from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    pg_username: str
    pg_password: str
    pg_host: str
    pg_port: int
    pg_database: str

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()
