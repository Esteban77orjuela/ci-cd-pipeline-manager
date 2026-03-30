from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Nombre de la aplicación
    APP_NAME: str = "CI/CD Pipeline Manager"
    VERSION: str = "0.1.0"
    DEBUG: bool = True

    # Esto lo llenaremos después con Supabase
    DATABASE_URL: str = ""

    # Esto lo llenaremos después con Groq
    GROQ_API_KEY: str = ""

    class Config:
        env_file = ".env"


# Creamos UNA sola instancia que usaremos en todo el proyecto
settings = Settings()