# Proyecto de Administración de Proyectos y Tareas con Listas Doblemente Enlazadas

## Descripción del Proyecto

Este proyecto es una implementación de un sistema de administración de proyectos utilizando listas doblemente enlazadas. En este sistema, cada proyecto tiene una lista de tareas, donde cada tarea puede ser avanzando o retrocedida. A través de las listas doblemente enlazadas, se pueden insertar y eliminar tareas en cualquier punto de la lista, lo que da flexibilidad para administrar las tareas de un proyecto.

### Funcionalidades Implementadas:

1. **Agregar un nuevo proyecto**: Permite crear un nuevo proyecto con un ID y nombre único.
2. **Agregar tarea al inicio de un proyecto**: Inserta una nueva tarea al principio de la lista de tareas de un proyecto.
3. **Agregar tarea al final de un proyecto**: Inserta una nueva tarea al final de la lista de tareas de un proyecto.
4. **Insertar tarea en una posición específica**: Permite insertar una tarea en cualquier posición dentro de la lista de tareas de un proyecto.
5. **Eliminar tarea**: Permite eliminar cualquier tarea de un proyecto, ajustando las conexiones de los nodos en la lista doblemente enlazada.
6. **Recorrer tareas de un proyecto**: Muestra las tareas de un proyecto en orden desde el principio hasta el final de la lista.
7. **Recorrer tareas de un proyecto de forma inversa**: Muestra las tareas de un proyecto en orden desde el final hasta el principio de la lista.

## Estructura del Código

El código está organizado en varias clases principales:

- **Clase Tarea**: Representa una tarea dentro de un proyecto, con un nombre, una descripción y un estado (pendiente, en progreso, completada).
- **Clase NodoTarea**: Representa cada nodo en la lista doblemente enlazada, que contiene una tarea y punteros a los nodos anterior y siguiente.
- **Clase Proyecto**: Representa un proyecto que contiene una lista doblemente enlazada de tareas y varios métodos para manipular las tareas.


