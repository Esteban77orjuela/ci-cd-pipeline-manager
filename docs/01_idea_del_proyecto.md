# Idea del proyecto (en simple)

Este proyecto es un backend (una API) que sirve para administrar automatizaciones internas de una empresa de software.

Una automatización típica es: tomar el código → revisar que esté bien (calidad) → correr pruebas → construir → publicar.

Ese “plan de pasos” se llama pipeline. Este proyecto guarda y organiza esos pipelines en una base de datos y expone endpoints para manejarlos.

## Conceptos clave

- Pipeline: la receta (qué se va a hacer y en qué orden).
- Ejecución (run): cada vez que esa receta se corre. Una ejecución tiene estado (pendiente, corriendo, falló, exitoso) y deja logs.
- CI: integración continua. Automatiza revisiones y pruebas cada vez que hay cambios.
- CD: entrega/despliegue continuo. Automatiza publicar cambios si pasan los controles.

## Qué hace hoy el repo

- Permite crear, listar, consultar, actualizar y eliminar pipelines.
- Guarda los pipelines en base de datos.

## Qué haremos después

- Agregar ejecuciones reales (runs), colas de trabajo y logs.
- Agregar Docker para desarrollo, pruebas automáticas, y CI en GitHub.
