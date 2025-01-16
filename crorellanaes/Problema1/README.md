# Administración de Proyectos con Listas Enlazadas

## Propósito del Proyecto

El propósito de este proyecto es diseñar y desarrollar un sistema de administración de proyectos utilizando listas enlazadas, de acuerdo con el enunciado del examen de la Semana 10. En este sistema, cada proyecto tiene un nombre, un ID único y una lista de tareas asociadas. Cada tarea tiene un nombre, una descripción y un estado (pendiente, en progreso, completada). Se implementan las siguientes funcionalidades utilizando listas enlazadas:

- Agregar un nuevo proyecto.
- Agregar tareas a un proyecto específico.
- Cambiar el estado de una tarea dentro de un proyecto.
- Listar todos los proyectos con sus respectivas tareas y estados.

## ¿Cómo Funciona el Código?

### Estructura General

El sistema está compuesto por clases que representan las entidades de proyectos y tareas, y la implementación de una lista enlazada para almacenar proyectos y sus respectivas tareas.

1. **Clases:**
   - **`Tarea`:** Representa una tarea dentro de un proyecto. Tiene un nombre, una descripción y un estado (pendiente, en progreso o completada).
   - **`Proyecto`:** Representa un proyecto con un ID y nombre, y contiene una lista de tareas.
   - **`ListaProyectos`:** Implementa una lista enlazada para gestionar varios proyectos.

2. **Funcionalidades:**
   - **Agregar un proyecto:** Permite crear un nuevo proyecto con un ID y nombre.
   - **Agregar una tarea:** Permite agregar tareas a un proyecto, con su nombre y descripción.
   - **Cambiar el estado de una tarea:** Permite cambiar el estado de una tarea a pendiente, en progreso o completada.
   - **Listar proyectos y tareas:** Muestra todos los proyectos registrados junto con sus tareas y sus estados actuales.

### Estructura de Archivos

El proyecto está compuesto por un solo archivo Python (`proyectos.py`), donde se gestionan todas las funcionalidades de la administración de proyectos. Las funcionalidades están implementadas en una única estructura interactiva, donde el usuario puede elegir entre diferentes opciones desde un menú.
