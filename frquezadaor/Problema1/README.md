# Sistema de Administración de Proyectos

## Propósito del Proyecto

El **Sistema de Administración de Proyectos** es una aplicación basada en consola que permite gestionar proyectos y sus respectivas tareas. Cada proyecto tiene un conjunto de tareas asociadas, y es posible agregar nuevas tareas, cambiar el estado de las tareas y listar todos los proyectos junto con sus tareas. 

## Cómo Funciona el Código

El código está estructurado en varias clases que simulan una lista enlazada de proyectos y tareas:

- **Clase `Tarea`:** Representa una tarea dentro de un proyecto. Cada tarea tiene un nombre, una descripción y un estado (pendiente, en progreso, completada). Además, cada tarea está enlazada a la siguiente tarea.
  
- **Clase `Proyecto`:** Representa un proyecto que tiene un nombre, un ID único y una lista de tareas (implementada como una lista enlazada). Un proyecto puede tener múltiples tareas y se puede agregar tareas o cambiar el estado de tareas existentes.

- **Clase `SistemaProyectos`:** Es la clase principal que gestiona todos los proyectos. Mantiene una lista enlazada de proyectos y permite agregar nuevos proyectos, listar todos los proyectos y sus tareas, y cambiar el estado de las tareas dentro de los proyectos.

- **Interfaz de Usuario:** El sistema presenta un menú interactivo que permite al usuario realizar varias acciones:
  1. Agregar un nuevo proyecto.
  2. Agregar una tarea a un proyecto existente.
  3. Cambiar el estado de una tarea.
  4. Listar todos los proyectos y sus tareas.
  5. Salir de la aplicación.

