class Tarea:
    def __init__(self, nombre, descripcion, estado='pendiente'):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in ['pendiente', 'en progreso', 'completada']:
            self.estado = nuevo_estado
        else:
            raise ValueError("Estado invalido. Use: 'pendiente', 'en progreso' o 'completada'.")

    def __str__(self):
        return f"Tarea: {self.nombre} | Estado: {self.estado} | Descripcion: {self.descripcion}"


class NodoTarea:
    def __init__(self, tarea):
        self.tarea = tarea
        self.siguiente = None


class Proyecto:
    def __init__(self, id_proyecto, nombre):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.tareas = None  # Lista enlazada de tareas.

    def agregar_tarea(self, nombre_tarea, descripcion):
        nueva_tarea = NodoTarea(Tarea(nombre_tarea, descripcion))
        if self.tareas is None:
            self.tareas = nueva_tarea
        else:
            actual = self.tareas
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva_tarea

    def cambiar_estado_tarea(self, nombre_tarea, nuevo_estado):
        actual = self.tareas
        while actual:
            if actual.tarea.nombre == nombre_tarea:
                actual.tarea.cambiar_estado(nuevo_estado)
                return
            actual = actual.siguiente
        raise ValueError(f"Tarea '{nombre_tarea}' no encontrada en el proyecto.")

    def listar_tareas(self):
        actual = self.tareas
        while actual:
            print(actual.tarea)
            actual = actual.siguiente

    def __str__(self):
        return f"Proyecto: {self.nombre} (ID: {self.id_proyecto})"


class NodoProyecto:
    def __init__(self, proyecto):
        self.proyecto = proyecto
        self.siguiente = None


class ListaProyectos:
    def __init__(self):
        self.cabeza = None  # Lista enlazada de proyectos.

    def agregar_proyecto(self, id_proyecto, nombre):
        nuevo_proyecto = NodoProyecto(Proyecto(id_proyecto, nombre))
        if self.cabeza is None:
            self.cabeza = nuevo_proyecto
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_proyecto

    def buscar_proyecto(self, id_proyecto):
        actual = self.cabeza
        while actual:
            if actual.proyecto.id_proyecto == id_proyecto:
                return actual.proyecto
            actual = actual.siguiente
        raise ValueError(f"Proyecto con ID '{id_proyecto}' no encontrado.")

    def listar_proyectos(self):
        actual = self.cabeza
        while actual:
            print(actual.proyecto)
            actual.proyecto.listar_tareas()
            actual = actual.siguiente


# Programa principal

def menu():
    lista_proyectos = ListaProyectos()

    while True:
        print("\n=== Sistema de Administracion de Proyectos ===")
        print("1. Agregar un nuevo proyecto")
        print("2. Agregar tarea a un proyecto")
        print("3. Cambiar el estado de una tarea")
        print("4. Listar todos los proyectos y tareas")
        print("5. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            id_proyecto = int(input("ID del proyecto: "))
            nombre = input("Nombre del proyecto: ")
            lista_proyectos.agregar_proyecto(id_proyecto, nombre)
            print("Proyecto agregado con exito.")

        elif opcion == "2":
            id_proyecto = int(input("ID del proyecto: "))
            try:
                proyecto = lista_proyectos.buscar_proyecto(id_proyecto)
                nombre_tarea = input("Nombre de la tarea: ")
                descripcion = input("Descripcion de la tarea: ")
                proyecto.agregar_tarea(nombre_tarea, descripcion)
                print("Tarea agregada con exito.")
            except ValueError as e:
                print(e)

        elif opcion == "3":
            id_proyecto = int(input("ID del proyecto: "))
            try:
                proyecto = lista_proyectos.buscar_proyecto(id_proyecto)
                nombre_tarea = input("Nombre de la tarea: ")
                nuevo_estado = input("Nuevo estado (pendiente, en progreso, completada): ")
                proyecto.cambiar_estado_tarea(nombre_tarea, nuevo_estado)
                print("Estado de la tarea actualizado con exito.")
            except ValueError as e:
                print(e)

        elif opcion == "4":
            print("\nListado de proyectos y tareas:")
            lista_proyectos.listar_proyectos()

        elif opcion == "5":
            print("Saliendo del sistema.")
            break

        else:
            print("Opcion invalida. Intenta de nuevo.")


# Ejecutar el programa
if __name__ == "__main__":
    menu()
