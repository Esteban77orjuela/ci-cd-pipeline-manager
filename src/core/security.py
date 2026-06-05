"""
Módulo de Seguridad — Fase 7 DevSecOps
Implementa autenticación por API Key usando el patrón de inyección
de dependencias de FastAPI (Dependency Injection).
"""

from fastapi import Depends, HTTPException, Security, status
from fastapi.security import APIKeyHeader

from src.core.config import Settings, get_settings

# Define el header HTTP que espera la API Key
# El cliente debe enviar: X-API-Key: <tu_clave>
API_KEY_HEADER = APIKeyHeader(name="X-API-Key", auto_error=False)


def verificar_api_key(
    api_key: str | None = Security(API_KEY_HEADER),
    settings: Settings = Depends(get_settings),
) -> str:
    """
    Dependencia de seguridad. Verifica que el header X-API-Key sea válido.

    En modo DEBUG (desarrollo), si API_KEY está vacía, se omite la verificación.
    En producción (DEBUG=False), la clave es SIEMPRE obligatoria.
    """
    # Modo desarrollo: si no hay key configurada, dejamos pasar
    if settings.DEBUG and not settings.API_KEY:
        return "dev-mode"

    # Modo producción (o dev con key configurada): verificar estrictamente
    if not api_key or api_key != settings.API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API Key inválida o ausente. Incluye el header: X-API-Key: <tu_clave>",
            headers={"WWW-Authenticate": "ApiKey"},
        )

    return api_key
