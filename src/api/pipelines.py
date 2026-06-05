from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.models.pipeline import Pipeline
from src.models.run import PipelineRun
from src.schemas.pipeline import PipelineCreate, PipelineResponse, PipelineUpdate
from src.schemas.run import PipelineRunCreate, PipelineRunResponse

router = APIRouter()


@router.get("/pipelines")
def obtener_pipelines(db: Session = Depends(get_db)):
    pipelines = db.query(Pipeline).all()

    return {
        "total": len(pipelines),
        "pipelines": pipelines,
    }


@router.post("/pipelines", response_model=dict)
def crear_pipeline(data: PipelineCreate, db: Session = Depends(get_db)):
    nuevo_pipeline = Pipeline(
        nombre=data.nombre, repositorio=data.repositorio
    )

    db.add(nuevo_pipeline)
    db.commit()
    db.refresh(nuevo_pipeline)

    pipeline_respuesta = PipelineResponse.model_validate(nuevo_pipeline)

    return {
        "mensaje": "Pipeline creado exitosamente ✅",
        "pipeline": pipeline_respuesta,
    }


@router.get("/pipelines/{id}")
def obtener_pipeline(id: int, db: Session = Depends(get_db)):
    pipeline = db.query(Pipeline).filter(Pipeline.id == id).first()

    if not pipeline:
        raise HTTPException(status_code=404, detail="Pipeline no encontrado")

    return pipeline


@router.put("/pipelines/{id}")
def actualizar_pipeline(id: int, data: PipelineUpdate, db: Session = Depends(get_db)):
    pipeline = db.query(Pipeline).filter(Pipeline.id == id).first()

    if not pipeline:
        raise HTTPException(status_code=404, detail="Pipeline no encontrado")

    if data.nombre is not None:
        pipeline.nombre = data.nombre

    if data.repositorio is not None:
        pipeline.repositorio = data.repositorio

    # Eliminado data.estado ya que ahora pertenece a las Runs
    
    db.commit()
    db.refresh(pipeline)

    return {
        "mensaje": "Pipeline actualizado ✅",
        "pipeline": PipelineResponse.model_validate(pipeline),
    }

@router.post("/pipelines/{id}/runs", response_model=dict)
def crear_run(id: int, db: Session = Depends(get_db)):
    pipeline = db.query(Pipeline).filter(Pipeline.id == id).first()
    if not pipeline:
        raise HTTPException(status_code=404, detail="Pipeline no encontrado")

    nuevo_run = PipelineRun(pipeline_id=id, estado="pendiente")
    db.add(nuevo_run)
    db.commit()
    db.refresh(nuevo_run)

    return {
        "mensaje": "Run iniciado exitosamente 🏃",
        "run": PipelineRunResponse.model_validate(nuevo_run)
    }

@router.get("/pipelines/{id}/runs")
def obtener_runs(id: int, db: Session = Depends(get_db)):
    pipeline = db.query(Pipeline).filter(Pipeline.id == id).first()
    if not pipeline:
        raise HTTPException(status_code=404, detail="Pipeline no encontrado")

    return {
        "total": len(pipeline.runs),
        "runs": [PipelineRunResponse.model_validate(run) for run in pipeline.runs]
    }


@router.delete("/pipelines/{id}")
def eliminar_pipeline(id: int, db: Session = Depends(get_db)):
    pipeline = db.query(Pipeline).filter(Pipeline.id == id).first()

    if not pipeline:
        raise HTTPException(status_code=404, detail="Pipeline no encontrado")

    db.delete(pipeline)
    db.commit()

    return {"mensaje": "Pipeline eliminado ✅"}
