from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.models.pipeline import Pipeline
from src.schemas.pipeline import PipelineCreate, PipelineResponse

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


@router.post("/pipelines", response_model=dict)
def crear_pipeline(data: PipelineCreate, db: Session = Depends(get_db)):
    nuevo_pipeline = Pipeline(
        nombre=data.nombre,
        repositorio=data.repositorio,
        estado="pendiente"
    )

    db.add(nuevo_pipeline)
    db.commit()
    db.refresh(nuevo_pipeline)

    pipeline_respuesta = PipelineResponse(
        id=nuevo_pipeline.id,
        nombre=nuevo_pipeline.nombre,
        repositorio=nuevo_pipeline.repositorio,
        estado=nuevo_pipeline.estado
    )

    return {
        "mensaje": "Pipeline creado exitosamente ✅",
        "pipeline": pipeline_respuesta
    }
    
@router.get("/pipelines/{id}")
def obtener_pipeline(id: int, db: Session = Depends(get_db)):
    pipeline = db.query(Pipeline).filter(Pipeline.id == id).first()

    if not pipeline:
        raise HTTPException(status_code=404, detail="Pipeline no encontrado")

    return {
        "id": pipeline.id,
        "nombre": pipeline.nombre,
        "repositorio": pipeline.repositorio,
        "estado": pipeline.estado
    }