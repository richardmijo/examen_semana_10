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

