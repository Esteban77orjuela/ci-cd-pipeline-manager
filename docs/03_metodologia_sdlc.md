# Metodología y Ciclo de Vida del Desarrollo de Software (SDLC)

Este documento define la estructura profesional estándar (basada en prácticas de Ingeniería de Software, Agile, y DevSecOps) que rige el ciclo de vida de este proyecto. Esta metodología es universal y aplicable a cualquier proyecto escalable en el mundo.

## FASE 0 — VISIÓN DEL PRODUCTO
**Idea General del Proyecto:** Un backend (API) para administrar y orquestar pipelines de automatización (CI/CD) internos.
- **Problema que resuelve:** La necesidad de centralizar, estandarizar y auditar cómo se construye y despliega el código en la empresa, evitando procesos manuales propensos a errores.
- **Valor que entrega:** Velocidad, consistencia y trazabilidad en el ciclo de desarrollo.
- **Objetivo de Negocio:** Reducir tiempos de salida a producción (Time-to-Market) y aumentar la confiabilidad de los despliegues.

## FASE 1 — REQUERIMIENTOS
- **Funcionales:** CRUD de pipelines, ejecución de pipelines (runs), recolección de logs, colas de trabajo.
- **No Funcionales:** Alta disponibilidad, baja latencia en la API, ejecución asíncrona de tareas pesadas, trazabilidad (logs).

## FASE 2 — ARQUITECTURA
- **Patrón:** Arquitectura por capas (API, Servicios, Repositorios) evolucionando hacia Clean Architecture.
- **Base de Datos:** PostgreSQL (relacional) para consistencia en configuraciones y estados de ejecución.
- **Asincronía:** Colas de mensajes (ej. Redis/Celery o similar) para procesar los "runs" sin bloquear la API.

## FASE 3 — DISEÑO TÉCNICO
- **Estructura:** Separación clara entre enrutadores (routers), lógica de negocio (services), y acceso a datos (repositories).
- **Contratos:** FastAPI con Pydantic para validación estricta de DTOs.

## FASE 4 — DESARROLLO
- **Estándares:** Clean Code, tipado estricto en Python.
- **Herramientas:** Ruff (linter/formatter), control de versiones mediante Git Trunk Based Development.

## FASE 5 — BASE DE DATOS
- **Gestión:** Uso de SQLAlchemy (ORM) y Alembic para migraciones y control de versiones del esquema relacional.

## FASE 6 — TESTING
- **Herramientas:** Pytest para unit testing e integration testing. Test Automation en cada PR.

## FASE 7 — CIBERSEGURIDAD (DEVSECOPS)
- **Implementación:** Manejo seguro de secretos (variables de entorno), inyección de dependencias seguras, validación de inputs estricta.

## FASE 8 — DOCKER Y CONTAINERS
- **Empaquetado:** Uso de `Dockerfile` para la API y los workers, orquestación local con `docker-compose`. Todo entorno debe ser 100% reproducible.

## FASE 9 — CI/CD
- **Pipeline del Proyecto:** Uso de GitHub Actions para correr pruebas automáticas, linters y preparar el despliegue automático.

## FASE 10 — CLOUD
- **Despliegue:** Preparación para despliegue en contenedores (AWS ECS, Kubernetes, etc.) según escale la necesidad.

## FASE 11 — OBSERVABILIDAD
- **Monitoreo:** Logs estructurados. Preparación para métricas de éxito/fallo de pipelines.

## FASE 12 — ESCALABILIDAD
- **Estrategia:** Escalado horizontal de los "workers" que ejecutan los pipelines, separando la carga de trabajo de la API de gestión.

## FASE 13 — MANTENIMIENTO Y EVOLUCIÓN
- **Prácticas:** Refactorización continua, gestión de deuda técnica y mejora iterativa de features.
