from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.models.pipeline import Pipeline

router = APIRouter()


@router.get("/pipelines")
def obtener_pipelines(db: Session = Depends(get_db)):
    pipelines = db.query(Pipeline).all()

    return {
        "total": len(pipelines),
        "pipelines": [
            {
                "id": pipeline.id,
                "nombre": pipeline.nombre,
                "repositorio": pipeline.repositorio,
                "estado": pipeline.estado
            }
            for pipeline in pipelines
        ]
    }


@router.post("/pipelines")
def crear_pipeline(nombre: str, repositorio: str, db: Session = Depends(get_db)):
    nuevo_pipeline = Pipeline(
        nombre=nombre,
        repositorio=repositorio,
        estado="pendiente"
    )

    db.add(nuevo_pipeline)
    db.commit()
    db.refresh(nuevo_pipeline)

    return {
        "mensaje": "Pipeline creado exitosamente ✅",
        "pipeline": {
            "id": nuevo_pipeline.id,
            "nombre": nuevo_pipeline.nombre,
            "repositorio": nuevo_pipeline.repositorio,
            "estado": nuevo_pipeline.estado
        }
    }