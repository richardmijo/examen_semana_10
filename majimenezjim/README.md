# Proyecto de Administración de Proyectos con Listas Enlazadas

Este proyecto implementa un sistema de administración de proyectos utilizando diferentes tipos de listas enlazadas para gestionar tareas asociadas a cada proyecto. El proyecto está dividido en cuatro problemas que utilizan listas enlazadas de diferentes maneras para gestionar los proyectos y sus tareas de forma eficiente.

## Propósito del Proyecto
El propósito del proyecto es demostrar el uso de listas enlazadas (simples, circulares y doblemente enlazadas) para gestionar la información de los proyectos y sus tareas en un sistema de administración. A través de estos problemas, se implementan operaciones básicas y avanzadas de listas enlazadas, como agregar tareas, modificar su estado, recorrer cíclicamente las tareas y generar tareas automáticamente mediante recursividad.

## Desarrollo del Proyecto

### Problema 1: Administración de Proyectos con Listas Enlazadas
En este problema, se implementó una lista enlazada simple para representar proyectos, donde cada proyecto tiene un ID único, un nombre y una lista de tareas asociadas. Cada tarea tiene un nombre, una descripción y un estado (pendiente, en progreso, completada). Las funcionalidades implementadas son:
- Agregar un nuevo proyecto.
- Agregar tareas a un proyecto específico.
- Cambiar el estado de una tarea dentro de un proyecto.
- Listar todos los proyectos con sus respectivas tareas y estados.

**Estructura utilizada**: Lista enlazada simple para los proyectos, donde cada nodo contiene un proyecto y una lista enlazada de tareas asociadas.

### Problema 2: Circularización de Tareas (Listas Circulares)
En este problema, se modificó la estructura de las tareas de los proyectos para convertir la lista de tareas en una lista circular. Esto permite recorrer cíclicamente las tareas de un proyecto de forma continua. Además, se implementó la posibilidad de eliminar tareas en cualquier punto de la lista circular.

**Estructura utilizada**: Lista circular para representar las tareas dentro de un proyecto. La lista circular permite que al llegar al último nodo, se vuelva al primero, creando un recorrido infinito.

### Problema 3: Planeación en Dos Direcciones (Listas Doblemente Enlazadas)
En este problema, se rediseñó la estructura de las tareas de los proyectos utilizando listas doblemente enlazadas. Esto permite:
- Avanzar y retroceder entre las tareas.
- Insertar tareas en cualquier posición dentro de la lista.
- Borrar tareas desde cualquier punto de la lista.

**Estructura utilizada**: Lista doblemente enlazada para las tareas, donde cada nodo tiene referencias tanto al nodo siguiente como al nodo anterior, permitiendo una navegación bidireccional.

### Problema 4: Generación Automática de Tareas (Recursividad)
En este último problema, se implementó una función recursiva para generar automáticamente tareas dentro de un rango de IDs proporcionado por el usuario. Cada tarea se inserta en la lista doblemente enlazada. La generación de tareas se realiza sin el uso de bucles, aprovechando la recursividad para crear las tareas de forma dinámica.

**Estructura utilizada**: Lista doblemente enlazada, utilizando recursividad para la inserción automática de tareas.

## Cómo Funciona el Código
El sistema permite interactuar con los proyectos y tareas a través de una serie de funciones que permiten al usuario agregar, modificar, eliminar y listar proyectos y tareas. Además, los problemas utilizan diferentes estructuras de listas enlazadas para gestionar las tareas de los proyectos de manera eficiente.

### Pasos para Ejecutar el Proyecto
1. **Clonar o Descargar el Repositorio**: Descarga o clona este proyecto en tu máquina local.
2. **Abrir el Código en un Editor**: Abre los archivos del proyecto en tu editor de texto o IDE preferido.
3. **Ejecutar el Programa**: 
   - Asegúrate de tener instalado Python 3.x en tu sistema.
   - Ejecuta el archivo `main.py` desde la terminal o el IDE con el siguiente comando:
     ```
     python main.py
     ```
4. **Interactuar con el Programa**: A medida que se ejecuta el programa, podrás ingresar los datos necesarios a través de la consola, como el nombre del proyecto, las tareas, y los estados de las tareas. Además, se podrá interactuar con las listas de tareas (circular o doblemente enlazada).




