from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class PipelineRunCreate(BaseModel):
    # Por ahora no pedimos datos extra para crear un run
    pass


class PipelineRunResponse(BaseModel):
    id: int
    pipeline_id: int
    estado: str
    fecha_creacion: datetime
    fecha_fin: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
