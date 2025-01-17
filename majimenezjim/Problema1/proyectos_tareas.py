class Tarea:
    def __init__(self, nombre, descripcion, estado="pendiente"):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado

    def __str__(self):

        return f"Tarea: {self.nombre}, Descripcion: {self.descripcion}, Estado: {self.estado}"


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:  # Si la lista esta vacia
            self.cabeza = nuevo_nodo
        else:  # Recorrer hasta el final y agregar el nodo
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def listar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato)
            actual = actual.siguiente


class Proyecto:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.tareas = ListaEnlazada()

    def __str__(self):
        return f"Proyecto ID: {self.id}, Nombre: {self.nombre}"


class SistemaDeProyectos:
    def __init__(self):
        self.proyectos = ListaEnlazada()

    def agregar_proyecto(self, id, nombre):
        proyecto = Proyecto(id, nombre)
        self.proyectos.agregar(proyecto)
        print(f"Proyecto '{nombre}' agregado con exito.")

    def agregar_tarea(self, id_proyecto, nombre_tarea, descripcion):
        actual = self.proyectos.cabeza
        while actual:
            if actual.dato.id == id_proyecto:
                tarea = Tarea(nombre_tarea, descripcion)
                actual.dato.tareas.agregar(tarea)
                print(f"Tarea '{nombre_tarea}' agregada al proyecto '{actual.dato.nombre}'.")
                return
            actual = actual.siguiente
        print(f"Proyecto con ID {id_proyecto} no encontrado.")

    def cambiar_estado_tarea(self, id_proyecto, nombre_tarea, nuevo_estado):
        actual = self.proyectos.cabeza
        while actual:
            if actual.dato.id == id_proyecto:
                tarea_actual = actual.dato.tareas.cabeza
                while tarea_actual:
                    if tarea_actual.dato.nombre == nombre_tarea:
                        tarea_actual.dato.estado = nuevo_estado
                        print(f"Estado de la tarea '{nombre_tarea}' cambiado a '{nuevo_estado}'.")
                        return
                    tarea_actual = tarea_actual.siguiente
                print(f"Tarea '{nombre_tarea}' no encontrada en el proyecto '{actual.dato.nombre}'.")
                return
            actual = actual.siguiente
        print(f"Proyecto con ID {id_proyecto} no encontrado.")

    def listar_proyectos(self):
        actual = self.proyectos.cabeza
        if not actual:
            print("No hay proyectos registrados.")
        while actual:
            print(actual.dato)  # Imprime el proyecto
            tarea_actual = actual.dato.tareas.cabeza
            while tarea_actual:
                print(f"  - {tarea_actual.dato}")
                tarea_actual = tarea_actual.siguiente
            actual = actual.siguiente


def menu():
    sistema = SistemaDeProyectos()

    while True:
        print("\nMenu de Administracion de Proyectos")
        print("1. Agregar un nuevo proyecto")
        print("2. Agregar una tarea a un proyecto")
        print("3. Cambiar el estado de una tarea")
        print("4. Listar todos los proyectos con sus tareas")
        print("5. Salir")
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            id_proyecto = int(input("Ingresa el ID del proyecto: "))
            nombre_proyecto = input("Ingresa el nombre del proyecto: ")
            sistema.agregar_proyecto(id_proyecto, nombre_proyecto)

        elif opcion == "2":
            id_proyecto = int(input("Ingresa el ID del proyecto: "))
            nombre_tarea = input("Ingresa el nombre de la tarea: ")
            descripcion_tarea = input("Ingresa la descripcion de la tarea: ")
            sistema.agregar_tarea(id_proyecto, nombre_tarea, descripcion_tarea)

        elif opcion == "3":
            id_proyecto = int(input("Ingresa el ID del proyecto: "))
            nombre_tarea = input("Ingresa el nombre de la tarea: ")
            nuevo_estado = input("Ingresa el nuevo estado (pendiente/en progreso/completada): ")
            sistema.cambiar_estado_tarea(id_proyecto, nombre_tarea, nuevo_estado)

        elif opcion == "4":
            sistema.listar_proyectos()

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opcion no valida, intenta nuevamente.")


if __name__ == "__main__":
    menu()
