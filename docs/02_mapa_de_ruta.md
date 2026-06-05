# Mapa de ruta

## Fase 1: Base profesional mínima

- Formato y lint automático (ruff).
- Pruebas (pytest) y una prueba “smoke” para confirmar que la API responde.
- Archivo `.env.example` para que cualquiera pueda arrancar sin adivinar variables.

## Fase 2: Entorno de desarrollo con Docker

- Postgres en `docker-compose`.
- Variables por ambiente: desarrollo, test, producción.

## Fase 3: CI en GitHub (calidad automática)

- Workflow que corra lint y tests en cada push y pull request.

## Fase 4: Arquitectura por capas

- Separar API (endpoints) de la lógica (servicios) y de la base de datos (repositorios).
- Manejo consistente de errores y validaciones.

## Fase 5: Migraciones de base de datos

- Alembic para versionar cambios del esquema.

## Fase 6: Pipeline “real”

- Modelo de datos para ejecuciones (runs) y logs.
- Worker/cola para ejecutar tareas sin bloquear la API.
- Estados, reintentos, timeouts y almacenamiento de resultados.

## Fase 7: Seguridad y operación

- Gestión de secretos, escaneo de dependencias, políticas en GitHub.
- Logs estructurados, health checks, métricas básicas.
