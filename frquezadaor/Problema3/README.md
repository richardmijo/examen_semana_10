# Sistema de Administración de Proyectos con Listas Doblemente Enlazadas

## Propósito del Proyecto

Este proyecto implementa un sistema de administración de proyectos utilizando **listas doblemente enlazadas**. Esto permite gestionar proyectos y tareas de manera eficiente, con la capacidad de avanzar y retroceder entre tareas.
## Cómo Funciona el Código

El código está organizado en las siguientes clases:
- **Clase `Tarea`:** Representa cada tarea en un proyecto. Cada tarea tiene un nombre, una descripción, un estado y dos punteros (`siguiente` y `anterior`) para permitir la navegación hacia adelante y hacia atrás.
  
- **Clase `Proyecto`:** Representa un proyecto. Contiene una lista doblemente enlazada de tareas y proporciona métodos para agregar tareas, insertar tareas en una posición específica, eliminar tareas y recorrer las tareas de manera secuencial o reversa.

- **Clase `SistemaProyectos`:** Administra los proyectos de manera global, permitiendo agregar proyectos, listar todos los proyectos y realizar operaciones sobre ellos.

El sistema proporciona un menú interactivo para gestionar los proyectos y tareas.
