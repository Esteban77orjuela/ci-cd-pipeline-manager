from pydantic import BaseModel


class PipelineCreate(BaseModel):
    nombre: str
    repositorio: str


class PipelineResponse(BaseModel):
    id: int
    nombre: str
    repositorio: str
    estado: str