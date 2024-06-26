from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    env_name: str = "local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./urls.db"

    class Config:
        env_file = ".str"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for {settings.env_name}")
    return settings
