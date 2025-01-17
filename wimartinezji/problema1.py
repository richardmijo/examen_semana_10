class Tarea:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = "Pendiente"
        self.siguiente = None

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

class ListaTareas:
    def __init__(self):
        self.cabeza = None

    def agregar_tarea(self, nombre, descripcion):
        nueva_tarea = Tarea(nombre, descripcion)
        if not self.cabeza:
            self.cabeza = nueva_tarea
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva_tarea

    def cambiar_estado_tarea(self, nombre_tarea, nuevo_estado):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre_tarea:
                actual.cambiar_estado(nuevo_estado)
                return True
            actual = actual.siguiente
        return False

    def listar_tareas(self):
        actual = self.cabeza
        while actual:
            print(f"  - Tarea: {actual.nombre} | Estado: {actual.estado} | Descripción: {actual.descripcion}")
            actual = actual.siguiente

class Proyecto:
    def __init__(self, nombre, id_proyecto):
        self.nombre = nombre
        self.id_proyecto = id_proyecto
        self.tareas = ListaTareas()
        self.siguiente = None

class ListaProyectos:
    def __init__(self):
        self.cabeza = None

    def agregar_proyecto(self, nombre, id_proyecto):
        nuevo_proyecto = Proyecto(nombre, id_proyecto)
        if not self.cabeza:
            self.cabeza = nuevo_proyecto
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_proyecto

    def agregar_tarea_a_proyecto(self, id_proyecto, nombre_tarea, descripcion):
        actual = self.cabeza
        while actual:
            if actual.id_proyecto == id_proyecto:
                actual.tareas.agregar_tarea(nombre_tarea, descripcion)
                return True
            actual = actual.siguiente
        return False

    def cambiar_estado_tarea(self, id_proyecto, nombre_tarea, nuevo_estado):
        actual = self.cabeza
        while actual:
            if actual.id_proyecto == id_proyecto:
                return actual.tareas.cambiar_estado_tarea(nombre_tarea, nuevo_estado)
            actual = actual.siguiente
        return False

    def listar_proyectos(self):
        actual = self.cabeza
        while actual:
            print(f"Proyecto: {actual.nombre} (ID: {actual.id_proyecto})")
            actual.tareas.listar_tareas()
            print("-")
            actual = actual.siguiente

# Menú de usuario
if __name__ == "__main__":
    sistema = ListaProyectos()
    
    while True:
        print("\nGestión de Proyectos")
        print("1. Agregar un nuevo proyecto")
        print("2. Agregar una tarea a un proyecto")
        print("3. Cambiar el estado de una tarea")
        print("4. Listar todos los proyectos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre del proyecto: ")
            id_proyecto = int(input("Ingrese el ID del proyecto: "))
            sistema.agregar_proyecto(nombre, id_proyecto)
        
        elif opcion == "2":
            id_proyecto = int(input("Ingrese el ID del proyecto: "))
            nombre_tarea = input("Ingrese el nombre de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            if not sistema.agregar_tarea_a_proyecto(id_proyecto, nombre_tarea, descripcion):
                print("Proyecto no encontrado.")
        
        elif opcion == "3":
            id_proyecto = int(input("Ingrese el ID del proyecto: "))
            nombre_tarea = input("Ingrese el nombre de la tarea: ")
            nuevo_estado = input("Ingrese el nuevo estado (Pendiente, En progreso, Completada): ")
            if not sistema.cambiar_estado_tarea(id_proyecto, nombre_tarea, nuevo_estado):
                print("Tarea o proyecto no encontrado.")
        
        elif opcion == "4":
            sistema.listar_proyectos()
        
        elif opcion == "5":
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")
