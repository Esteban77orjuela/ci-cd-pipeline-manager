from functools import lru_cache

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Nombre de la aplicación
    APP_NAME: str = "CI/CD Pipeline Manager"
    VERSION: str = "0.1.0"
    DEBUG: bool = True

    # Base de datos
    DATABASE_URL: str = "sqlite:///./local.db"

    # API Key para autenticación (obligatoria en producción)
    API_KEY: str = ""

    # Integración con Groq (IA)
    GROQ_API_KEY: str = ""

    model_config = SettingsConfigDict(env_file=".env")

    @model_validator(mode="after")
    def validar_produccion(self) -> "Settings":
        """En producción, la API_KEY no puede estar vacía."""
        if not self.DEBUG and not self.API_KEY:
            raise ValueError(
                "API_KEY es obligatoria cuando DEBUG=False (modo producción). "
                "Configura la variable de entorno API_KEY."
            )
        return self


@lru_cache
def get_settings() -> Settings:
    return Settings()
