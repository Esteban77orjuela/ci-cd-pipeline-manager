from fastapi import FastAPI
from src.core.config import settings
from src.api.pipelines import router as pipelines_router
from src.core.database import Base, engine
from src.models.pipeline import Pipeline

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    description="API para gestionar despliegues y automatización",
    version=settings.VERSION
)

app.include_router(pipelines_router)


@app.get("/")
def ruta_principal():
    return {
        "mensaje": f"¡{settings.APP_NAME} iniciado con éxito! 🚀",
        "estado": "Activo",
        "version": settings.VERSION
    }