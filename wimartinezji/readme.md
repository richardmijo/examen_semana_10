# Examen Semana 10

## Problema 1: Gestión de Proyectos y Tareas con Listas Enlazadas

### Descripción
Este programa permite gestionar proyectos y sus tareas utilizando listas enlazadas en Python. Cada proyecto tiene un nombre, un ID único y una lista de tareas asociadas. Cada tarea posee un nombre, una descripción y un estado que puede cambiarse entre "Pendiente", "En progreso" y "Completada". 

### Clases
- **Tarea**: Representa una tarea con nombre, descripción y estado.
- **ListaTareas**: Maneja una lista enlazada de tareas.
- **Proyecto**: Representa un proyecto con un ID único y una lista de tareas asociadas.
- **ListaProyectos**: Administra múltiples proyectos y permite operaciones como agregar proyectos, agregar tareas y cambiar estados.

### Funcionalidades
El código proporciona un menú interactivo en la línea de comandos para realizar las siguientes operaciones:
1. Agregar un nuevo proyecto.
2. Agregar una tarea a un proyecto.
3. Cambiar el estado de una tarea.
4. Listar todos los proyectos y sus tareas.
5. Salir del programa.

---

## Problema 2: Gestión de Tareas con Lista Circular

### Descripción
El propósito de este código es simular un sistema de gestión de tareas mediante una lista circular. Se busca implementar un ciclo continuo de tareas que permite recorrerlas de forma cíclica, agregar nuevas tareas y eliminar tareas en cualquier punto de la lista.

### Funciones Principales
- **Agregar tarea**: El usuario puede agregar una tarea a la lista circular.
- **Ver tareas**: El usuario puede ver las tareas de forma cíclica, es decir, las tareas se mostrarán de forma continua.
- **Eliminar tarea**: El usuario puede eliminar cualquier tarea de la lista en cualquier punto.
- **Salir**: El usuario puede salir del programa.

---

## Problema 3: Gestión de Tareas con Lista Doblemente Enlazada

### Descripción
El propósito de este código es representar las tareas mediante una lista doblemente enlazada. Esta estructura de datos permite:
- Avanzar y retroceder entre tareas.
- Insertar tareas en cualquier posición dentro de la lista.
- Eliminar tareas desde cualquier punto de la lista.

### Funciones Principales
- **Agregar tarea**: El usuario puede agregar una tarea al final de la lista.
- **Insertar tarea**: El usuario puede insertar una tarea en una posición específica dentro de la lista.
- **Ver tareas (avanzar)**: El usuario puede ver las tareas avanzando desde el primer nodo.
- **Ver tareas (retroceder)**: El usuario puede ver las tareas retrocediendo desde el último nodo.
- **Eliminar tarea**: El usuario puede eliminar cualquier tarea de la lista.
- **Salir**: El usuario puede salir del programa.

---

## Problema 4: Generación Automática de Tareas con Recursividad

### Descripción
El objetivo de este código es gestionar una lista de tareas utilizando listas doblemente enlazadas. Esto permite avanzar y retroceder entre tareas, insertar y eliminar tareas en cualquier posición, y generar automáticamente tareas en un rango determinado usando recursividad.

### Estructura de la Lista
La lista implementa una estructura doblemente enlazada, donde cada tarea está representada por un nodo que contiene los siguientes atributos:
- `tarea`: El nombre o descripción de la tarea.
- `siguiente`: Un puntero al siguiente nodo (tarea).
- `anterior`: Un puntero al nodo anterior (tarea).

### Funciones Principales
- **Agregar tarea**: Se agrega una tarea al final de la lista.
- **Insertar tarea en una posición específica**: Se puede insertar una tarea en cualquier posición dentro de la lista.
- **Eliminar tarea**: Permite eliminar una tarea de la lista, buscando por nombre.
- **Recorrer las tareas**: Permite recorrer las tareas de la lista tanto hacia adelante como hacia atrás.
- **Generación automática de tareas**: Usando recursividad, se generan tareas en un rango de IDs con una descripción base, y se insertan en la lista.

---

**Autor:** Wilson Rene Martínez Jiménez  
**Fecha:** 16 de Enero 2025
