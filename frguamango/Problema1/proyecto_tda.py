class Tarea:
    def __init__(self, nombre, descripcion, estado="Pendiente"):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado
        self.siguiente = None

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

    def cambiar_estado(self, nombre_tarea, nuevo_estado):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre_tarea:
                actual.estado = nuevo_estado
                return True
            actual = actual.siguiente
        return False

    def listar_tareas(self):
        actual = self.cabeza
        tareas = []
        while actual:
            tareas.append(f"{actual.nombre} - {actual.descripcion} - {actual.estado}")
            actual = actual.siguiente
        return tareas

class Proyecto:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.tareas = ListaTareas()
        self.siguiente = None

class ListaProyectos:
    def __init__(self):
        self.cabeza = None

    def agregar_proyecto(self, id, nombre):
        nuevo_proyecto = Proyecto(id, nombre)
        if not self.cabeza:
            self.cabeza = nuevo_proyecto
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_proyecto

    def obtener_proyecto(self, id):
        actual = self.cabeza
        while actual:
            if actual.id == id:
                return actual
            actual = actual.siguiente
        return None

    def listar_proyectos(self):
        actual = self.cabeza
        proyectos = []
        while actual:
            proyectos.append(f"{actual.id} - {actual.nombre}")
            tareas = actual.tareas.listar_tareas()
            for tarea in tareas:
                proyectos.append(f"  {tarea}")
            actual = actual.siguiente
        return proyectos

# Programa principal
def main():
    lista_proyectos = ListaProyectos()

    while True:
        print("\n--- Menú ---")
        print("1. Agregar proyecto")
        print("2. Agregar tarea a proyecto")
        print("3. Cambiar estado de tarea")
        print("4. Listar proyectos y tareas")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            id = input("ID del proyecto: ")
            nombre = input("Nombre del proyecto: ")
            lista_proyectos.agregar_proyecto(id, nombre)

        elif opcion == "2":
            id = input("ID del proyecto: ")
            proyecto = lista_proyectos.obtener_proyecto(id)
            if proyecto:
                nombre_tarea = input("Nombre de la tarea: ")
                descripcion = input("Descripción de la tarea: ")
                proyecto.tareas.agregar_tarea(nombre_tarea, descripcion)
            else:
                print("Proyecto no encontrado.")

        elif opcion == "3":
            id = input("ID del proyecto: ")
            proyecto = lista_proyectos.obtener_proyecto(id)
            if proyecto:
                nombre_tarea = input("Nombre de la tarea: ")
                nuevo_estado = input("Nuevo estado (Pendiente/En progreso/Completada): ")
                if not proyecto.tareas.cambiar_estado(nombre_tarea, nuevo_estado):
                    print("Tarea no encontrada.")
            else:
                print("Proyecto no encontrado.")

        elif opcion == "4":
            proyectos = lista_proyectos.listar_proyectos()
            for proyecto in proyectos:
                print(proyecto)

        elif opcion == "5":
            break

        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
