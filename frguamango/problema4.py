class TareaDoble:
    def __init__(self, nombre, descripcion, estado="Pendiente"):
        # Inicializa una tarea con nombre, descripción y estado
        self.nombre = nombre  # Nombre de la tarea
        self.descripcion = descripcion  # Descripción de la tarea
        self.estado = estado  # Estado de la tarea (Pendiente, En progreso, Completada)
        self.anterior = None  # Referencia al nodo anterior
        self.siguiente = None  # Referencia al nodo siguiente

class ListaDobleTareas:
    def __init__(self):
        # Inicializa una lista doblemente enlazada vacía
        self.cabeza = None  # Referencia a la primera tarea
        self.cola = None  # Referencia a la última tarea

    def agregar_tarea(self, nombre, descripcion):
        # Agrega una nueva tarea al final de la lista doblemente enlazada
        nueva_tarea = TareaDoble(nombre, descripcion)  # Crear nueva tarea
        if not self.cabeza:  # Si la lista está vacía
            self.cabeza = nueva_tarea  # La nueva tarea se convierte en la cabeza
            self.cola = nueva_tarea  # También se convierte en la cola
        else:
            nueva_tarea.anterior = self.cola  # La nueva tarea apunta al nodo actual de la cola
            self.cola.siguiente = nueva_tarea  # La cola actual apunta a la nueva tarea
            self.cola = nueva_tarea  # Actualiza la cola a la nueva tarea

    def listar_tareas(self):
        # Lista todas las tareas con sus detalles
        actual = self.cabeza
        tareas = []
        while actual:  # Recorre la lista de la cabeza a la cola
            tareas.append(f"{actual.nombre} - {actual.descripcion} - {actual.estado}")
            actual = actual.siguiente
        return tareas

class ProyectoDoble:
    def __init__(self, id, nombre):
        # Inicializa un proyecto con ID único, nombre y una lista doblemente enlazada de tareas
        self.id = id  # ID único del proyecto
        self.nombre = nombre  # Nombre del proyecto
        self.tareas = ListaDobleTareas()  # Lista doblemente enlazada de tareas asociadas al proyecto

class ListaProyectosDobles:
    def __init__(self):
        # Inicializa una lista enlazada vacía para proyectos
        self.cabeza = None

    def agregar_proyecto(self, id, nombre):
        # Agrega un nuevo proyecto al final de la lista enlazada
        nuevo_proyecto = ProyectoDoble(id, nombre)  # Crear nuevo proyecto
        if not self.cabeza:  # Si la lista está vacía
            self.cabeza = nuevo_proyecto  # El nuevo proyecto se convierte en la cabeza
        else:
            actual = self.cabeza
            while actual.siguiente:  # Recorre hasta el último nodo
                actual = actual.siguiente
            actual.siguiente = nuevo_proyecto  # Agrega el nuevo proyecto al final

    def obtener_proyecto(self, id):
        # Busca un proyecto por su ID en la lista enlazada
        actual = self.cabeza  # Inicia desde la cabeza
        while actual:  # Recorre la lista
            if actual.id == id:  # Si encuentra el proyecto por su ID
                return actual  # Retorna el proyecto
            actual = actual.siguiente
        return None  # Retorna None si no encuentra el proyecto

# Función recursiva para generar tareas automáticamente
def generar_tareas_recursivamente(lista_tareas, id_inicio, id_fin, descripcion_base):
    if id_inicio > id_fin:
        # Caso base: si el inicio supera el final, detiene la recursión
        return
    # Genera el nombre y descripción de la tarea actual
    nombre_tarea = f"Tarea {id_inicio}"
    descripcion_tarea = f"{descripcion_base} {id_inicio}"
    # Agrega la tarea a la lista doblemente enlazada
    lista_tareas.agregar_tarea(nombre_tarea, descripcion_tarea)
    # Llamada recursiva para la siguiente tarea
    generar_tareas_recursivamente(lista_tareas, id_inicio + 1, id_fin, descripcion_base)

# Programa principal
def main():
    lista_proyectos = ListaProyectosDobles()  # Inicializa la lista enlazada de proyectos

    while True:
        print("\n--- Menú ---")
        print("1. Agregar proyecto")
        print("2. Generar tareas automáticamente")
        print("3. Listar proyectos y tareas")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            # Agregar un nuevo proyecto
            id = input("ID del proyecto: ")
            nombre = input("Nombre del proyecto: ")
            lista_proyectos.agregar_proyecto(id, nombre)

        elif opcion == "2":
            # Generar tareas automáticamente para un proyecto
            id = input("ID del proyecto: ")
            proyecto = lista_proyectos.obtener_proyecto(id)
            if proyecto:
                id_inicio = int(input("ID inicial de las tareas: "))
                id_fin = int(input("ID final de las tareas: "))
                descripcion_base = input("Descripción base de las tareas: ")
                # Llama a la función recursiva para generar las tareas
                generar_tareas_recursivamente(proyecto.tareas, id_inicio, id_fin, descripcion_base)
                print("Tareas generadas correctamente.")
            else:
                print("Proyecto no encontrado.")

        elif opcion == "3":
            # Listar todos los proyectos y sus tareas
            actual = lista_proyectos.cabeza
            while actual:
                print(f"Proyecto {actual.id} - {actual.nombre}")
                tareas = actual.tareas.listar_tareas()
                for tarea in tareas:
                    print(f"  {tarea}")
                actual = actual.siguiente

        elif opcion == "4":
            # Salir del programa
            break

        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
