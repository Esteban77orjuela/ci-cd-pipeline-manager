# 🚀 CI/CD Pipeline Manager

Sistema de gestión de pipelines de integración y despliegue continuo.

## Tecnologías

- **Backend:** Python + FastAPI
- **Base de datos:** Supabase (PostgreSQL)
- **Frontend:** React (deploy en Vercel)
- **Tareas async:** Celery + Redis
- **IA:** Groq API

## Estado

🟡 En desarrollo

## Documentación

- [Idea del proyecto](docs/01_idea_del_proyecto.md)
- [Mapa de ruta](docs/02_mapa_de_ruta.md)

## Ejecución local (rápido)

1. Crea un archivo `.env` tomando como base `.env.example`.
2. Instala dependencias:
   - `pip install -r requirements.txt`
3. Ejecuta la API:
   - `uvicorn src.main:app --reload`

## Base de datos local con Docker

1. Levanta Postgres:
   - `docker compose up -d`
2. Verifica que tu `.env` tenga `DATABASE_URL` apuntando a Postgres (mira `.env.example`).
