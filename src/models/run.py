from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

from src.core.database import Base


class PipelineRun(Base):
    __tablename__ = "pipeline_runs"

    id = Column(Integer, primary_key=True, index=True)
    pipeline_id = Column(Integer, ForeignKey("pipelines.id"), nullable=False)
    estado = Column(String, default="pendiente", nullable=False)
    fecha_creacion = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    fecha_fin = Column(DateTime, nullable=True)

    pipeline = relationship("Pipeline", back_populates="runs")
