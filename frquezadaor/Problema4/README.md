# Sistema de Administración de Proyectos con Generación Automática de Tareas

## Propósito del Proyecto

Este proyecto implementa un sistema de administración de proyectos que permite la creación automática de tareas mediante recursividad. 

## Cómo Funciona el Código

El código está dividido en varias clases que trabajan juntas para lograr la funcionalidad deseada:

- **Clase `Tarea`:** Representa una tarea dentro de un proyecto. Cada tarea tiene un nombre, una descripción, un estado y dos punteros (`siguiente` y `anterior`) para permitir la navegación tanto hacia adelante como hacia atrás.

- **Clase `Proyecto`:** Representa un proyecto. Contiene una lista doblemente enlazada de tareas y tiene métodos para agregar tareas, insertar tareas en posiciones específicas.

- **Clase `SistemaProyectos`:** Administra todos los proyectos. Permite agregar proyectos y listar los proyectos existentes en el sistema.

- **Función recursiva `generar_tareas_recursivo`:** Dada una descripción base y un rango de IDs, esta función crea tareas de manera recursiva y las inserta en la lista doblemente enlazada de un proyecto.

