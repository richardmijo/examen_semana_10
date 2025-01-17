# Administración de Proyectos

## Propósito del Proyecto
El propósito de este proyecto es implementar un sistema de administración de proyectos utilizando estructuras de datos manuales (listas enlazadas, circulares y doblemente enlazadas) que permiten gestionar proyectos y sus tareas asociadas. Cada tarea tiene un nombre, descripción y estado (Pendiente, En progreso, Completada). Este proyecto se divide en cuatro problemas específicos que abordan diferentes tipos de estructuras y funcionalidades.

## Cómo funciona el código
El sistema está dividido en cuatro partes:

1. **Problema 1: Administración de Proyectos con Listas Enlazadas**
   - Implementa listas enlazadas para manejar proyectos y sus tareas.
   - Permite agregar proyectos, asignar tareas, cambiar el estado de tareas y listar todos los proyectos con sus tareas.

2. **Problema 2: Circularización de Tareas**
   - Convierte la lista de tareas en una estructura circular para recorrerlas continuamente.
   - Permite agregar tareas, eliminarlas y recorrerlas en ciclos.

3. **Problema 3: Planeación en Dos Direcciones**
   - Utiliza listas doblemente enlazadas para manejar las tareas dentro de cada proyecto.
   - Permite avanzar y retroceder entre tareas, insertar tareas en cualquier posición y eliminarlas desde cualquier punto.

4. **Problema 4: Generación Automática de Tareas**
   - Implementa una función recursiva para generar tareas automáticamente en un rango de IDs.
   - Las tareas se agregan automáticamente a la lista doblemente enlazada del proyecto seleccionado.

## Pasos para Ejecutar el Proyecto
1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/richardmijo/examen_semana_10.git
   cd examen_semana_10/frguamango
   ```

2. **Ejecutar el programa principal**:
   - Cada problema tiene un archivo independiente. Por ejemplo, para ejecutar el problema 1:
     ```bash
     python problema1_listas_enlazadas.py
     ```

3. **Interacción con el menú**:
   - Sigue las instrucciones del menú para realizar las operaciones permitidas, como agregar proyectos, tareas, o listar información.

## Ejemplos de Entrada y Salida

### Problema 1: Listas Enlazadas
**Entrada:**
- Agregar un proyecto con ID `1` y nombre `Proyecto A`.
- Agregar una tarea al proyecto `1` con nombre `Tarea 1` y descripción `Primera tarea`.
- Cambiar el estado de `Tarea 1` a `En progreso`.
- Listar proyectos.

**Salida:**
```
1 - Proyecto A
  Tarea 1 - Primera tarea - En progreso
```

### Problema 2: Listas Circulares
**Entrada:**
- Agregar un proyecto con ID `1` y nombre `Proyecto Circular`.
- Agregar tareas al proyecto `1`.
- Recorrer las tareas cíclicamente 2 veces.

**Salida:**
```
Tarea 1 - Descripción 1 - Pendiente
Tarea 2 - Descripción 2 - Pendiente
Tarea 1 - Descripción 1 - Pendiente
Tarea 2 - Descripción 2 - Pendiente
```

### Problema 3: Listas Doblemente Enlazadas
**Entrada:**
- Agregar un proyecto con ID `1` y nombre `Proyecto Planeación`.
- Insertar tareas en posiciones específicas.
- Eliminar una tarea.
- Listar tareas del proyecto.

**Salida:**
```
1 - Proyecto Planeación
  Tarea 1 - Descripción 1 - Pendiente
  Tarea 3 - Descripción 3 - En progreso
```

### Problema 4: Generación Automática de Tareas
**Entrada:**
- Agregar un proyecto con ID `1` y nombre `Proyecto Recursivo`.
- Generar tareas automáticamente con IDs del `1` al `5` y descripción base `Auto-generada`.
- Listar tareas.

**Salida:**
```
1 - Proyecto Recursivo
  Tarea 1 - Auto-generada 1 - Pendiente
  Tarea 2 - Auto-generada 2 - Pendiente
  Tarea 3 - Auto-generada 3 - Pendiente
  Tarea 4 - Auto-generada 4 - Pendiente
  Tarea 5 - Auto-generada 5 - Pendiente
