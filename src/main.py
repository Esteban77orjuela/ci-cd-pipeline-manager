from fastapi import FastAPI

from src.api.pipelines import router as pipelines_router
from src.core.config import get_settings
from src.core.database import Base, engine
from src.models import Pipeline, PipelineRun

# _ = Pipeline
# _ = PipelineRun

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    description="API para gestionar despliegues y automatización",
    version=settings.VERSION,
)

app.include_router(pipelines_router)


@app.get("/")
def ruta_principal():
    return {
        "mensaje": f"¡{settings.APP_NAME} iniciado con éxito! 🚀",
        "estado": "Activo",
        "version": settings.VERSION,
    }
