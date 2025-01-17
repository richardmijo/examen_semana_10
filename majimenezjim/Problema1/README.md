## Administracion de Proyectos con Listas Enlazadas
Proposito del Proyecto
Este proyecto es una aplicacion interactiva para administrar proyectos y sus tareas asociadas. El objetivo es demostrar el uso de listas enlazadas implementadas manualmente (sin bibliotecas externas) para gestionar datos dinamicos como proyectos y tareas. Cada proyecto contiene una lista de tareas, y estas pueden tener diferentes estados (pendiente, en progreso, completada).

Como Funciona el Codigo
El sistema utiliza las siguientes clases principales:

Tarea: Representa una tarea con un nombre, descripcion y estado.
Nodo: Es el elemento basico de una lista enlazada, que contiene un dato (como un proyecto o una tarea) y un puntero al siguiente nodo.
ListaEnlazada: Implementa una lista enlazada manualmente, permitiendo agregar nodos y recorrer la lista.
Proyecto: Representa un proyecto con un ID unico, nombre y una lista enlazada de tareas.
SistemaDeProyectos: Contiene todas las operaciones principales, como agregar proyectos, agregar tareas, cambiar el estado de tareas y listar proyectos.

Funcionalidades
Agregar un nuevo proyecto: Crea un proyecto con un ID unico y un nombre.
Agregar tareas a un proyecto especifico: Añade una tarea con un nombre y descripcion a un proyecto existente.
Cambiar el estado de una tarea: Actualiza el estado de una tarea especifica dentro de un proyecto.
Listar proyectos con sus tareas y estados: Muestra todos los proyectos con sus respectivas tareas y sus estados.

Restricciones
El sistema no utiliza bibliotecas externas para las listas enlazadas, lo que permite comprender como funcionan a nivel interno.