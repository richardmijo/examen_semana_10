# problema 1
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
# problema 2
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


# problema 3
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



# problema 4
# Proyecto de Generación Automática de Tareas con Recursividad

## Descripción del Proyecto

Este proyecto implementa un sistema de administración de proyectos utilizando listas doblemente enlazadas. La principal funcionalidad añadida en este ejercicio es la **generación automática de tareas** usando una función recursiva.

La función recursiva permite crear tareas dentro de un proyecto, dada una descripción base y un rango de IDs para las tareas (por ejemplo, generar tareas con IDs del 1 al 5). Las tareas generadas se insertan automáticamente en la lista doblemente enlazada de un proyecto.

### Funcionalidades Implementadas:

1. **Agregar un nuevo proyecto**: Permite crear un nuevo proyecto con un ID y nombre único.
2. **Generar tareas automáticamente (recursivo)**: Permite generar una lista de tareas automáticamente, dada una descripción base y un rango de IDs. La función es completamente recursiva, sin utilizar bucles.
3. **Insertar tareas al final**: Las tareas generadas se insertan al final de la lista doblemente enlazada de tareas de cada proyecto.
4. **Recorrer tareas de un proyecto**: Muestra las tareas de un proyecto en orden normal (de principio a fin).
5. **Recorrer tareas de un proyecto de forma inversa**: Muestra las tareas de un proyecto en orden inverso (de fin a principio).

## Estructura del Código

El código está organizado en las siguientes clases principales:

- **Clase Tarea**: Representa una tarea dentro de un proyecto, con un nombre, una descripción y un estado (pendiente, en progreso, completada).
- **Clase NodoTarea**: Representa un nodo dentro de la lista doblemente enlazada, que contiene una tarea y referencias al nodo anterior y siguiente.
- **Clase Proyecto**: Representa un proyecto que contiene una lista doblemente enlazada de tareas. Esta clase permite agregar tareas, recorrer las tareas en ambas direcciones y generar tareas automáticamente usando recursividad.

