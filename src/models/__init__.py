from src.models.pipeline import Pipeline
from src.models.run import PipelineRun

# Esto asegura que SQLAlchemy registre los modelos en Base.metadata
__all__ = ["Pipeline", "PipelineRun"]
