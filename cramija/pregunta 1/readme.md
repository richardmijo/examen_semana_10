# Problema 1: Administración de Proyectos con Listas Enlazadas (TDA y Listas)

## Propósito del Proyecto
El objetivo de este proyecto es implementar un sistema de administración de proyectos utilizando una estructura de datos tipo lista enlazada. Cada proyecto puede tener una lista de tareas asociadas, permitiendo agregar, listar y cambiar el estado de las tareas. Este enfoque utiliza conceptos de Tipos Abstractos de Datos (TAD) y listas enlazadas, lo que permite manejar de manera eficiente las relaciones entre proyectos y sus respectivas tareas.

## Cómo Funciona el Código
El proyecto se basa en dos clases principales:

1. **Tarea**: Representa una tarea individual dentro de un proyecto, con atributos como nombre, descripción y estado.
2. **Proyecto**: Gestiona una lista de tareas asociadas a un proyecto específico. Incluye métodos para agregar tareas, listar tareas y cambiar el estado de una tarea.

### Funcionalidades Principales:
- **Agregar Tarea**: Permite añadir una nueva tarea a un proyecto.
- **Listar Tareas**: Muestra todas las tareas asociadas a un proyecto con sus estados.
- **Cambiar Estado de Tarea**: Modifica el estado de una tarea existente.

### Clases y Métodos:
- `class Tarea`: Clase que define las propiedades de una tarea (`nombre`, `descripcion`, `estado`).
- `class Proyecto`: Clase que gestiona la lista enlazada de tareas con métodos como `agregar_tarea`, `listar_tareas`, y `cambiar_estado_tarea`.

## Pasos para Ejecutar el Proyecto
1. **Clona el Repositorio**: Clona este repositorio en tu máquina local usando `git clone <url-del-repositorio>`.
2. **Navega al Directorio del Proyecto**: Usa `cd <nombre-del-directorio>` para moverte al directorio del proyecto.
3. **Ejecuta el Archivo Principal**: Ejecuta el archivo principal del proyecto usando Python con el comando `python <nombre-del-archivo>.py`.
4. **Sigue las Instrucciones del Menú**: Interactúa con el menú para agregar, listar o cambiar el estado de tareas dentro de un proyecto.

## Ejemplos de Entrada y Salida del Programa

### EJEMPLO DE ENTRADA
```plaintext
Menú de Administración de Proyectos
1. Agregar Tarea
2. Listar Tareas
3. Cambiar Estado de Tarea
4. Salir
Selecciona una opción: 1
Nombre del proyecto: Proyecto A
Nombre de la tarea: Tarea 1
Descripción de la tarea: Descripción de la Tarea 1
Tarea agregada exitosamente.

Menú de Administración de Proyectos
1. Agregar Tarea
2. Listar Tareas
3. Cambiar Estado de Tarea
4. Salir
Selecciona una opción: 2
Nombre del proyecto: Proyecto A
Listado de tareas:
Tarea: Tarea 1, Estado: pendiente


##EJEMPLO SALIDA:

Listado de tareas:
Tarea: Tarea 1, Estado: pendiente

Menú de Administración de Proyectos
1. Agregar Tarea
2. Listar Tareas
3. Cambiar Estado de Tarea
4. Salir
Selecciona una opción: 3
Nombre del proyecto: Proyecto A
Nombre de la tarea: Tarea 1
Nuevo estado: completada
Estado de la tarea 'Tarea 1' cambiado a 'completada'.







#EJERCICIO 2
# Proyecto de Lista Circular de Tareas

## Propósito del Proyecto
El propósito de este proyecto es implementar una lista circular para gestionar tareas de manera eficiente. La lista circular permite almacenar tareas con un nombre, descripción y estado, facilitando la adición, visualización y eliminación de tareas. Este proyecto es ideal para aprender sobre estructuras de datos como listas enlazadas circulares y su aplicación en la gestión de tareas.

## Cómo Funciona el Código
El proyecto consiste en dos clases principales:

1. **Tarea**: Representa una tarea con atributos para el nombre, descripción y estado. Cada tarea también apunta a la siguiente tarea en la lista circular.
2. **ListaCircular**: Implementa la lista circular con métodos para agregar, listar y eliminar tareas. 

El código también incluye un menú interactivo que permite al usuario interactuar con la lista circular mediante opciones para agregar, listar y eliminar tareas, así como salir del programa.

### Métodos Principales:
- `agregar_tarea(nombre, descripcion)`: Añade una nueva tarea a la lista circular.
- `listar_tareas_circular()`: Muestra todas las tareas en la lista circular.
- `eliminar_tarea(nombre)`: Elimina una tarea específica de la lista circular por su nombre.

## Pasos para Ejecutar el Proyecto
1. **Clona el Repositorio**: Clona este repositorio en tu máquina local usando `git clone <url-del-repositorio>`.
2. **Navega al Directorio del Proyecto**: Usa `cd <nombre-del-directorio>` para moverte al directorio del proyecto.
3. **Ejecuta el Programa**: Ejecuta el archivo principal del proyecto usando Python con el comando `python <nombre-del-archivo>.py`.
4. **Interactúa con el Menú**: Sigue las instrucciones en el menú interactivo para agregar, listar o eliminar tareas.

## Ejemplos de Entrada y Salida del Programa


```plaintext
Menú de Lista Circular
1. Agregar Tarea
2. Listar Tareas
3. Eliminar Tarea
4. Salir
Selecciona una opción: 1
Nombre de la tarea: Tarea 1
Descripción de la tarea: Descripción de la Tarea 1
Tarea agregada exitosamente.

Menú de Lista Circular
1. Agregar Tarea
2. Listar Tareas
3. Eliminar Tarea
4. Salir
Selecciona una opción: 2
Listado de tareas:
Tarea: Tarea 1, Descripción: Descripción de la Tarea 1, Estado: pendiente


### Ejemplo de Salida:

Listado de tareas:
Tarea: Tarea 1, Descripción: Descripción de la Tarea 1, Estado: pendiente

Menú de Lista Circular
1. Agregar Tarea
2. Listar Tareas
3. Eliminar Tarea
4. Salir
Selecciona una opción: 3
Nombre de la tarea a eliminar: Tarea 1
Tarea 'Tarea 1' eliminada.




##EJERCICIO 3

# Proyecto de Administración de Tareas con Listas Doblemente Enlazadas

## Descripción
Este proyecto gestiona tareas dentro de un **proyecto** utilizando una **lista doblemente enlazada**. Permite avanzar y retroceder entre tareas, insertar tareas en cualquier posición dentro de la lista, y borrar tareas desde cualquier punto de la lista.

## Funcionalidades
- **Avanzar y retroceder entre tareas**: Navega entre las tareas del proyecto hacia adelante o hacia atrás.
- **Insertar tareas en cualquier posición**: Puedes agregar tareas al inicio, final o en una posición específica dentro de la lista.
- **Eliminar tareas**: Permite eliminar cualquier tarea en la lista, independientemente de su posición.
- **Listar tareas**: Muestra todas las tareas actuales en el proyecto con su estado y descripción.

## Estructura de Datos
El sistema utiliza una **lista doblemente enlazada**, donde cada tarea está representada por un nodo que contiene:
- **nombre**: Nombre de la tarea.
- **descripción**: Descripción detallada de la tarea.
- **estado**: Estado de la tarea (por defecto es "pendiente").
- **siguiente**: Enlace al siguiente nodo (tarea).
- **anterior**: Enlace al nodo anterior (tarea).

## Clases
- **NodoTarea**: Representa cada tarea en la lista doblemente enlazada.
- **Proyecto**: Gestiona las tareas del proyecto mediante los métodos de inserción, eliminación, avance y retroceso.

## Instalación
1. Clona el repositorio o descarga los archivos.
2. Asegúrate de tener instalado Python 3.x.
3. Ejecuta el archivo `proyecto.py` desde la terminal o un entorno de desarrollo integrado (IDE).

## Uso
Al ejecutar el programa, el usuario podrá interactuar con el sistema mediante un menú con las siguientes opciones:

### Menú
1. **Insertar tarea al inicio**: Inserta una nueva tarea al principio de la lista.
2. **Insertar tarea al final**: Inserta una nueva tarea al final de la lista.
3. **Insertar tarea en una posición**: Inserta una nueva tarea en una posición específica.
4. **Listar tareas**: Muestra todas las tareas del proyecto con su estado.
5. **Eliminar tarea**: Elimina una tarea especificando su nombre.
6. **Avanzar a la siguiente tarea**: Navega hacia la siguiente tarea en la lista.
7. **Retroceder a la tarea anterior**: Retrocede a la tarea anterior en la lista.
8. **Salir**: Cierra el programa.

## Ejemplos de Entrada y Salida

### Entrada:




##EJERCICIO 4:

# Proyecto de Lista Circular de Tareas

## Propósito del Proyecto
El propósito de este proyecto es implementar una lista circular para gestionar tareas de manera eficiente. La lista circular permite almacenar tareas con un nombre, descripción y estado, facilitando la adición, visualización y eliminación de tareas. Este proyecto es ideal para aprender sobre estructuras de datos como listas enlazadas circulares y su aplicación en la gestión de tareas.

## Cómo Funciona el Código
El proyecto consta de dos clases principales:

1. **Tarea**: Representa una tarea con los siguientes atributos:
   - `nombre`: El nombre de la tarea (ej. "Tarea 1").
   - `descripcion`: Una descripción detallada de la tarea.
   - `estado`: El estado de la tarea (por ejemplo, "pendiente", "completada").

   Cada tarea está enlazada a la siguiente tarea mediante el atributo `siguiente`, lo que permite formar la lista circular.

2. **ListaCircular**: Implementa la lista circular con los siguientes métodos:
   - `agregar_tarea(nombre, descripcion)`: Añade una nueva tarea a la lista circular.
   - `listar_tareas_circular()`: Muestra todas las tareas en la lista circular.
   - `eliminar_tarea(nombre)`: Elimina una tarea específica de la lista circular por su nombre.

### Métodos Principales
- **agregar_tarea(nombre, descripcion)**: Agrega una nueva tarea a la lista circular. Si la lista está vacía, la nueva tarea será la primera y única tarea de la lista. Si ya hay tareas en la lista, la nueva tarea se inserta al final, y la lista sigue siendo circular.
  
- **listar_tareas_circular()**: Imprime todas las tareas almacenadas en la lista circular. Comienza desde la primera tarea y sigue hasta volver al inicio, garantizando que todas las tareas se muestren.

- **eliminar_tarea(nombre)**: Elimina una tarea por su nombre. Si la tarea está en la lista, se elimina y la lista se reorganiza para mantener su estructura circular.

## Pasos para Ejecutar el Proyecto

1. **Clona el Repositorio**: Si tienes Git instalado, puedes clonar este repositorio en tu máquina local usando el siguiente comando:

   ```bash
   git clone <url-del-repositorio>



Ejemplo de entrada
Menú de Lista Circular
1. Agregar Tarea
2. Listar Tareas
3. Eliminar Tarea
4. Salir
Selecciona una opción: 1
Nombre de la tarea: Tarea 1
Descripción de la tarea: Descripción de la Tarea 1
Tarea agregada exitosamente.

Menú de Lista Circular
1. Agregar Tarea
2. Listar Tareas
3. Eliminar Tarea
4. Salir
Selecciona una opción: 2
Listado de tareas:
Tarea: Tarea 1, Descripción: Descripción de la Tarea 1, Estado: pendiente

##EJEMPLO SALIDA:


Menú de Lista Circular
1. Agregar Tarea
2. Listar Tareas
3. Eliminar Tarea
4. Salir
Selecciona una opción: 3
Nombre de la tarea a eliminar: Tarea 1
Tarea eliminada exitosamente.

Menú de Lista Circular
1. Agregar Tarea
2. Listar Tareas
3. Eliminar Tarea
4. Salir
Selecciona una opción: 2
Listado de tareas:
(No hay tareas para mostrar)

