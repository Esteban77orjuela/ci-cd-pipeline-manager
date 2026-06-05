# Bitácora de Desarrollo del Proyecto

Esta bitácora registra el historial de desarrollo, decisiones arquitectónicas, tareas completadas y comandos importantes bajo el marco metodológico Scrum/Agile. El propósito es mantener una trazabilidad profesional (Fase 13 - Mantenimiento y Evolución).

## Sesión 1: Establecimiento de Metodología y Visión
**Fecha:** 2026-06-01

### ¿Qué se hizo?
1. **Validación de SDLC:** Se confirmó y adoptó el ciclo de vida de desarrollo de software (Fases 0 a 13) propuesto por el Arquitecto/Lead.
2. **Documentación:** Se creó el documento `docs/03_metodologia_sdlc.md` para anclar estas fases al contexto específico de nuestro proyecto (Gestor de Pipelines CI/CD).
3. **Bitácora:** Inicialización de este documento (`BITACORA.md`) para registrar el progreso paso a paso.

### Idea General y Particular (Feedback de Arquitectura)
- **Idea General (Visión de Negocio):** Necesitamos un sistema que sea el "cerebro" central de las automatizaciones de la empresa. Al igual que un aeropuerto necesita una torre de control para organizar los vuelos, una empresa de software necesita este proyecto (ci-cd-pipeline) para organizar y auditar cómo el código llega a producción.
- **Idea Particular (Implementación actual):** Hoy estamos en la etapa de formalizar el terreno. Hemos sentado las bases de *cómo* vamos a trabajar (las 14 fases) antes de empezar a programar (Fase 0 y 1). Escribimos la estructura metodológica en `03_metodologia_sdlc.md` para que cualquier ingeniero que se una al proyecto sepa exactamente qué estándares usamos.

### Próximos pasos
- Revisar el estado actual del código mediante pruebas de concepto (Smoke Test). -> **Hecho. 2 pruebas pasaron con éxito.**
- Iniciar la **Fase 4 (Desarrollo)** revisando la estructura del backend actual e instalando el entorno local de manera controlada.

## Sesión 2: Verificación de Entorno Base
**Fecha:** 2026-06-01

### ¿Qué se hizo?
1. **Activación de entorno:** Se activó el entorno virtual aislado (`venv`).
2. **Smoke Test:** Se ejecutó `pytest`. El resultado fue `2 passed`, confirmando que la estructura base de la API está sana.
3. **Arranque del Servidor (Fase 4):** Se levantó la API localmente utilizando el servidor `uvicorn`. El arranque fue exitoso (`Application startup complete`).
4. **Fase 5 (Migraciones) - Instalación:** Se instaló `alembic` en el entorno virtual y se deshabilitó la creación automática de tablas en `src/main.py`.
5. **Fase 5 (Migraciones) - Inicialización:** Se inicializó Alembic (`alembic init`) y se vinculó la conexión de la base de datos y los modelos de la app modificando `alembic/env.py`.
6. **Fase 5 (Migraciones) - Primera Migración:** Se generó la revisión automática (`bed49b7ab1f4`) y se aplicó a la base de datos con éxito. Con esto cerramos la base estructural de datos.

## Sesión 3: El Pipeline "Real" (Fase 6)
**Fecha:** 2026-06-01

### ¿Qué se hizo?
1. **Clean Architecture:** Se separó la entidad `Pipeline` (la receta) de la entidad `PipelineRun` (la ejecución real).
2. **Nuevos Endpoints:** Se implementaron los métodos POST y GET para las ejecuciones.
3. **Refactorización de Pruebas:** Se actualizaron las pruebas (`pytest`) para soportar la nueva arquitectura. Se solucionó un bug en las pruebas locales asegurando que la base de datos temporal de pruebas se recree en cada ejecución. También se actualizaron los esquemas de Pydantic a la versión V2 (ConfigDict) para eliminar warnings de deprecación.
4. **Corrección datetime:** Se reemplazó `datetime.utcnow` (deprecado en Python 3.12+) por `datetime.now(timezone.utc)`.
5. **Fix crítico en tests:** El reload de módulos en el entorno de prueba requería recargar los modelos en el orden correcto: `database` → `models` → `main`. Sin esto, `Base.metadata.create_all()` no conocía la tabla `pipeline_runs`.

---

## Sesión 4: DevSecOps, Docker y CI/CD (Fases 7, 8 y 9)
**Fecha:** 2026-06-05

### ¿Qué se hizo?

#### Fase 7 — Ciberseguridad (DevSecOps)
1. **API Key Authentication:** Se creó `src/core/security.py` con la dependencia `verificar_api_key`. Todos los endpoints quedan protegidos con una sola línea (`dependencies=[Depends(verificar_api_key)]`).
2. **Modo DEBUG seguro:** Si `DEBUG=False` y `API_KEY` está vacía, el servidor no arranca (validado con `@model_validator` en Pydantic).
3. **Validación estricta de inputs:** Se agregaron `Field(min_length, max_length)` y `AnyHttpUrl` a los schemas de Pipeline para rechazar datos malformados antes de llegar a la BD.

#### Fase 8 — Docker
1. **Dockerfile (multi-stage):** Etapa `builder` instala dependencias, etapa `runner` copia solo lo necesario → imagen liviana y segura.
2. **docker-compose.yml completo:** Orquesta los servicios `db` (PostgreSQL) y `api` (FastAPI). La API espera a que la DB esté sana (`service_healthy`) antes de arrancar y ejecuta las migraciones automáticamente.

#### Fase 9 — GitHub Actions CI
1. **Workflow mejorado:** Dos jobs paralelos independientes: `lint` (ruff) y `test` (pytest en Python 3.12 y 3.13).
2. **Variables de entorno en CI:** Se configuró `DEBUG=true` y `API_KEY=""` para que las pruebas no fallen por falta de credenciales en el entorno de GitHub Actions.

### Estado: ✅ `2 passed` — Pruebas en verde. Código en GitHub.

---
