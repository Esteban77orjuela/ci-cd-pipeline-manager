from pydantic import BaseModel, ConfigDict, Field, AnyHttpUrl
from typing import List, Optional
from src.schemas.run import PipelineRunResponse


class PipelineCreate(BaseModel):
    nombre: str = Field(
        min_length=3,
        max_length=100,
        description="Nombre del pipeline. Entre 3 y 100 caracteres.",
        examples=["deploy-produccion"],
    )
    repositorio: AnyHttpUrl = Field(
        description="URL completa del repositorio Git.",
        examples=["https://github.com/mi-empresa/mi-repo"],
    )


class PipelineResponse(BaseModel):
    id: int
    nombre: str
    repositorio: str
    runs: List[PipelineRunResponse] = []

    model_config = ConfigDict(from_attributes=True)


class PipelineUpdate(BaseModel):
    nombre: Optional[str] = Field(
        default=None,
        min_length=3,
        max_length=100,
        description="Nuevo nombre del pipeline.",
    )
    repositorio: Optional[AnyHttpUrl] = Field(
        default=None,
        description="Nueva URL del repositorio.",
    )
