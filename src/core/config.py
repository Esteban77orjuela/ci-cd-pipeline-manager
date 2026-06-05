from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Nombre de la aplicación
    APP_NAME: str = "CI/CD Pipeline Manager"
    VERSION: str = "0.1.0"
    DEBUG: bool = True

    # Esto lo llenaremos después con Supabase
    DATABASE_URL: str = "sqlite:///./local.db"

    # Esto lo llenaremos después con Groq
    GROQ_API_KEY: str = ""

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings() -> Settings:
    return Settings()
