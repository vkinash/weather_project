from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    env_name: str = "Local"
    db_url: str = "sqlite:///./weather.db"
    city: str = "Kyiv"
    latitude: float = .0
    longitude: float = .0
    # default values provided for code review convenience
    # ideally should be removed
    api_key: str = "17fe61111a3d5c289dfa7505eb46a034"
    x_token: str = "qIsJY*=lQr-X`|%+EVlf(9P-m+[/A3$3"

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
