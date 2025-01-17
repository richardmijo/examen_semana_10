# Sistema de Administración de Proyectos con Listas Circulares

## Propósito del Proyecto

Este proyecto implementa un sistema de administración de tareas dentro de un proyecto utilizando una **lista circular**. El objetivo es ofrecer un sistema cíclico de revisión de tareas, permitiendo agregar, eliminar y visualizar las tareas de manera continua, proporcionando una experiencia fluida de gestión de proyectos.

## Cómo Funciona el Código

El programa está basado en una estructura de **listas circulares**, donde cada tarea es representada por un nodo. Cada tarea tiene un nombre, una descripción y un estado, y está asociada con un proyecto. El código permite al usuario:
1. **Agregar una tarea**: Se puede agregar una nueva tarea a la lista de tareas de un proyecto.
2. **Recorrer las tareas cíclicamente**: Permite ver las tareas de un proyecto de manera continua, siguiendo el ciclo de la lista circular.
3. **Eliminar una tarea**: El usuario puede eliminar una tarea de cualquier parte de la lista.

### Estructura del Código
1. **Clase Tarea**: Representa una tarea con sus atributos `nombre`, `descripcion` y `estado`.
2. **Clase Nodo**: Representa un nodo en la lista circular que apunta a una tarea.
3. **Clase ListaCircular**: Gestiona la lista circular de tareas, proporcionando métodos para agregar, eliminar y recorrer las tareas.
4. **Función `main()`**: Interactúa con el usuario, permitiendo agregar, eliminar y ver las tareas de forma interactiva a través de un menú en consola.

