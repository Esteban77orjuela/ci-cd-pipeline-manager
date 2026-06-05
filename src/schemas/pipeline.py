from pydantic import BaseModel, ConfigDict
from typing import List
from src.schemas.run import PipelineRunResponse

class PipelineCreate(BaseModel):
    nombre: str
    repositorio: str


class PipelineResponse(BaseModel):
    id: int
    nombre: str
    repositorio: str
    runs: List[PipelineRunResponse] = []

    model_config = ConfigDict(from_attributes=True)


class PipelineUpdate(BaseModel):
    nombre: str = None
    repositorio: str = None
