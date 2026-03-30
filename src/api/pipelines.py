from fastapi import APIRouter

# APIRouter = Un "piso" nuevo en nuestro edificio
router = APIRouter()

# Base de datos temporal (después usaremos Supabase)
pipelines_db = []


@router.get("/pipelines")
def obtener_pipelines():
    return {
        "total": len(pipelines_db),
        "pipelines": pipelines_db
    }


@router.post("/pipelines")
def crear_pipeline(nombre: str, repositorio: str):
    nuevo_pipeline = {
        "id": len(pipelines_db) + 1,
        "nombre": nombre,
        "repositorio": repositorio,
        "estado": "pendiente"
    }
    pipelines_db.append(nuevo_pipeline)
    return {
        "mensaje": "Pipeline creado exitosamente ✅",
        "pipeline": nuevo_pipeline
    }