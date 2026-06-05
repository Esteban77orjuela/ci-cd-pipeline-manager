# ============================================================
# FASE 8 — Docker: Dockerfile de la API (Multi-stage build)
# ============================================================
# Usamos multi-stage build para mantener la imagen final liviana:
# - Etapa "builder": instala dependencias
# - Etapa "runner": solo copia lo necesario para producción

# ── Etapa 1: Builder ──────────────────────────────────────
FROM python:3.12-slim AS builder

WORKDIR /app

# Copiar requirements primero (aprovecha el cache de Docker)
COPY requirements.txt .

# Instalar dependencias en un directorio separado
RUN pip install --upgrade pip && \
    pip install --prefix=/install -r requirements.txt


# ── Etapa 2: Runner (imagen final) ────────────────────────
FROM python:3.12-slim AS runner

WORKDIR /app

# Copiar dependencias ya instaladas desde el builder
COPY --from=builder /install /usr/local

# Copiar el código de la aplicación
COPY src/ ./src/
COPY alembic/ ./alembic/
COPY alembic.ini .

# Variable de entorno: no generar archivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Puerto que expone la API
EXPOSE 8000

# Comando de inicio: ejecutar migraciones y luego levantar la API
CMD ["sh", "-c", "alembic upgrade head && uvicorn src.main:app --host 0.0.0.0 --port 8000"]
