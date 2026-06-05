from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.core.database import Base


class Pipeline(Base):
    __tablename__ = "pipelines"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    repositorio = Column(String, nullable=False)

    runs = relationship("PipelineRun", back_populates="pipeline", cascade="all, delete-orphan")
