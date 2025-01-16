# Circularización de Tareas con Listas Circulares

## Propósito del Proyecto

El propósito de este proyecto es implementar un sistema de gestión de tareas dentro de proyectos utilizando listas circulares. Este sistema permite recorrer cíclicamente las tareas de un proyecto, eliminar tareas en cualquier punto de la lista circular y gestionar la información asociada a cada tarea (como el estado de la tarea).

## ¿Cómo Funciona el Código?

### Estructura General

El sistema está compuesto por las siguientes clases:

1. **Tarea**: Representa una tarea dentro de un proyecto. Cada tarea tiene un nombre, descripción y estado (pendiente, en progreso o completada). Esta clase tiene un método para cambiar el estado de la tarea.

2. **NodoTarea**: Representa un nodo que contiene una tarea y un puntero al siguiente nodo, formando así la estructura de una lista circular.

3. **Proyecto**: Representa un proyecto que contiene una lista circular de tareas. Ofrece métodos para agregar tareas, eliminar tareas y recorrer las tareas cíclicamente.

4. **Menú Interactivo**: El sistema está diseñado con un menú interactivo que permite al usuario seleccionar entre varias opciones como agregar proyectos, agregar tareas, eliminar tareas, recorrer las tareas cíclicamente y listar todas las tareas de los proyectos.

### Funcionalidades Principales

1. **Agregar tarea**: Permite agregar una nueva tarea a un proyecto específico. Si es la primera tarea del proyecto, se forma la lista circular.

2. **Eliminar tarea**: Permite eliminar una tarea de cualquier punto dentro de la lista circular de tareas. El ciclo se mantiene intacto después de la eliminación.

3. **Recorrer tareas cíclicamente**: Permite recorrer la lista circular de tareas, mostrando cada tarea de forma continua.

4. **Listar proyectos y tareas**: Muestra todos los proyectos y sus respectivas tareas, indicando su estado y descripción.


