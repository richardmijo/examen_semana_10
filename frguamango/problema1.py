class Tarea:
    def __init__(self, nombre, descripcion, estado="Pendiente"):
        # Inicializa una tarea con nombre, descripción y estado predeterminado "Pendiente"
        self.nombre = nombre  # Nombre de la tarea
        self.descripcion = descripcion  # Descripción de la tarea
        self.estado = estado  # Estado de la tarea (Pendiente, En progreso, Completada)
        self.siguiente = None  # Referencia al siguiente nodo (tarea)

class ListaTareas:
    def __init__(self):
        # Inicializa una lista enlazada vacía para tareas
        self.cabeza = None

    def agregar_tarea(self, nombre, descripcion):
        # Agrega una nueva tarea al final de la lista enlazada
        nueva_tarea = Tarea(nombre, descripcion)  # Crear nueva tarea
        if not self.cabeza:  # Si la lista está vacía
            self.cabeza = nueva_tarea  # La nueva tarea se convierte en la cabeza
        else:
            actual = self.cabeza  # Inicia desde la cabeza
            while actual.siguiente:  # Recorre la lista hasta el último nodo
                actual = actual.siguiente
            actual.siguiente = nueva_tarea  # Agrega la nueva tarea al final

    def cambiar_estado(self, nombre_tarea, nuevo_estado):
        # Cambia el estado de una tarea específica por su nombre
        actual = self.cabeza  # Inicia desde la cabeza
        while actual:  # Recorre la lista
            if actual.nombre == nombre_tarea:  # Si encuentra la tarea por su nombre
                actual.estado = nuevo_estado  # Actualiza el estado
                return True  # Retorna True si se encontró y cambió el estado
            actual = actual.siguiente
        return False  # Retorna False si no encontró la tarea

    def listar_tareas(self):
        # Retorna una lista con todas las tareas y sus detalles
        actual = self.cabeza  # Inicia desde la cabeza
        tareas = []  # Lista para almacenar los detalles de las tareas
        while actual:  # Recorre la lista
            tareas.append(f"{actual.nombre} - {actual.descripcion} - {actual.estado}")
            actual = actual.siguiente
        return tareas

class Proyecto:
    def __init__(self, id, nombre):
        # Inicializa un proyecto con ID único, nombre y una lista de tareas
        self.id = id  # ID único del proyecto
        self.nombre = nombre  # Nombre del proyecto
        self.tareas = ListaTareas()  # Lista enlazada de tareas asociadas al proyecto
        self.siguiente = None  # Referencia al siguiente nodo (proyecto)

class ListaProyectos:
    def __init__(self):
        # Inicializa una lista enlazada vacía para proyectos
        self.cabeza = None

    def agregar_proyecto(self, id, nombre):
        # Agrega un nuevo proyecto al final de la lista enlazada
        nuevo_proyecto = Proyecto(id, nombre)  # Crear nuevo proyecto
        if not self.cabeza:  # Si la lista está vacía
            self.cabeza = nuevo_proyecto  # El nuevo proyecto se convierte en la cabeza
        else:
            actual = self.cabeza  # Inicia desde la cabeza
            while actual.siguiente:  # Recorre la lista hasta el último nodo
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

    def listar_proyectos(self):
        # Retorna una lista con todos los proyectos y sus tareas
        actual = self.cabeza  # Inicia desde la cabeza
        proyectos = []  # Lista para almacenar los detalles de los proyectos
        while actual:  # Recorre la lista
            proyectos.append(f"{actual.id} - {actual.nombre}")  # Agrega el proyecto actual
            tareas = actual.tareas.listar_tareas()  # Obtiene las tareas asociadas al proyecto
            for tarea in tareas:
                proyectos.append(f"  {tarea}")  # Agrega las tareas con indentación
            actual = actual.siguiente
        return proyectos

# Programa principal
def main():
    lista_proyectos = ListaProyectos()  # Inicializa la lista enlazada de proyectos

    while True:
        print("\n--- Menú ---")
        print("1. Agregar proyecto")
        print("2. Agregar tarea a proyecto")
        print("3. Cambiar estado de tarea")
        print("4. Listar proyectos y tareas")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            # Opción para agregar un nuevo proyecto
            id = input("ID del proyecto: ")
            nombre = input("Nombre del proyecto: ")
            lista_proyectos.agregar_proyecto(id, nombre)

        elif opcion == "2":
            # Opción para agregar una tarea a un proyecto existente
            id = input("ID del proyecto: ")
            proyecto = lista_proyectos.obtener_proyecto(id)  # Busca el proyecto por ID
            if proyecto:
                nombre_tarea = input("Nombre de la tarea: ")
                descripcion = input("Descripción de la tarea: ")
                proyecto.tareas.agregar_tarea(nombre_tarea, descripcion)  # Agrega la tarea al proyecto
            else:
                print("Proyecto no encontrado.")

        elif opcion == "3":
            # Opción para cambiar el estado de una tarea específica
            id = input("ID del proyecto: ")
            proyecto = lista_proyectos.obtener_proyecto(id)  # Busca el proyecto por ID
            if proyecto:
                nombre_tarea = input("Nombre de la tarea: ")
                nuevo_estado = input("Nuevo estado (Pendiente/En progreso/Completada): ")
                if not proyecto.tareas.cambiar_estado(nombre_tarea, nuevo_estado):
                    print("Tarea no encontrada.")  # Mensaje si la tarea no existe
            else:
                print("Proyecto no encontrado.")

        elif opcion == "4":
            # Opción para listar todos los proyectos y sus tareas
            proyectos = lista_proyectos.listar_proyectos()  # Obtiene todos los proyectos y tareas
            for proyecto in proyectos:
                print(proyecto)  # Imprime cada proyecto y sus tareas

        elif opcion == "5":
            # Salir del programa
            break

        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
