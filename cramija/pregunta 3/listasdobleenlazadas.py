class NodoTarea:
    def __init__(self, nombre, descripcion, estado="pendiente"):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado
        self.siguiente = None
        self.anterior = None

class Proyecto:
    def __init__(self, id_proyecto, nombre):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.tareas = None

    def insertar_tarea_inicio(self, nombre, descripcion, estado="pendiente"):
        nueva_tarea = NodoTarea(nombre, descripcion, estado)
        if not self.tareas:
            self.tareas = nueva_tarea
        else:
            nueva_tarea.siguiente = self.tareas
            self.tareas.anterior = nueva_tarea
            self.tareas = nueva_tarea

    def insertar_tarea_final(self, nombre, descripcion, estado="pendiente"):
        nueva_tarea = NodoTarea(nombre, descripcion, estado)
        if not self.tareas:
            self.tareas = nueva_tarea
        else:
            actual = self.tareas
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva_tarea
            nueva_tarea.anterior = actual

    def insertar_tarea_posicion(self, posicion, nombre, descripcion, estado="pendiente"):
        nueva_tarea = NodoTarea(nombre, descripcion, estado)
        if not self.tareas:
            self.tareas = nueva_tarea
        else:
            actual = self.tareas
            contador = 0
            while actual and contador < posicion:
                actual = actual.siguiente
                contador += 1

            if actual:
                nueva_tarea.siguiente = actual
                nueva_tarea.anterior = actual.anterior
                if actual.anterior:
                    actual.anterior.siguiente = nueva_tarea
                actual.anterior = nueva_tarea
            else:
                self.insertar_tarea_final(nombre, descripcion, estado)

    def listar_tareas(self):
        if not self.tareas:
            print("No hay tareas en el proyecto.")
            return
        actual = self.tareas
        while actual:
            print(f"Tarea: {actual.nombre}, Descripción: {actual.descripcion}, Estado: {actual.estado}")
            actual = actual.siguiente

    def eliminar_tarea(self, nombre):
        if not self.tareas:
            print("No hay tareas en el proyecto.")
            return
        actual = self.tareas
        while actual:
            if actual.nombre == nombre:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                if actual == self.tareas:
                    self.tareas = actual.siguiente
                del actual
                print(f"Tarea '{nombre}' eliminada.")
                return
            actual = actual.siguiente
        print(f"Tarea '{nombre}' no encontrada.")

    def avanzar(self, nombre):
        actual = self.tareas
        while actual:
            if actual.nombre == nombre:
                if actual.siguiente:
                    print(f"Avanzando a la tarea: {actual.siguiente.nombre}")
                    return actual.siguiente
                else:
                    print("No hay más tareas para avanzar.")
                    return actual
            actual = actual.siguiente
        print(f"Tarea '{nombre}' no encontrada.")
        return None

    def retroceder(self, nombre):
        actual = self.tareas
        while actual:
            if actual.nombre == nombre:
                if actual.anterior:
                    print(f"Retrocediendo a la tarea: {actual.anterior.nombre}")
                    return actual.anterior
                else:
                    print("No hay más tareas para retroceder.")
                    return actual
            actual = actual.siguiente
        print(f"Tarea '{nombre}' no encontrada.")
        return None


# MENU


def menu():
    proyecto = Proyecto(1, "Proyecto A")

    while True:
        print("\nMenú de Administración de Tareas")
        print("1. Insertar tarea al inicio")
        print("2. Insertar tarea al final")
        print("3. Insertar tarea en una posición")
        print("4. Listar tareas")
        print("5. Eliminar tarea")
        print("6. Avanzar a la siguiente tarea")
        print("7. Retroceder a la tarea anterior")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            proyecto.insertar_tarea_inicio(nombre, descripcion)
        elif opcion == "2":
            nombre = input("Nombre de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            proyecto.insertar_tarea_final(nombre, descripcion)
        elif opcion == "3":
            posicion = int(input("Posición en la lista: "))
            nombre = input("Nombre de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            proyecto.insertar_tarea_posicion(posicion, nombre, descripcion)
        elif opcion == "4":
            proyecto.listar_tareas()
        elif opcion == "5":
            nombre = input("Nombre de la tarea a eliminar: ")
            proyecto.eliminar_tarea(nombre)
        elif opcion == "6":
            nombre = input("Nombre de la tarea a avanzar: ")
            proyecto.avanzar(nombre)
        elif opcion == "7":
            nombre = input("Nombre de la tarea a retroceder: ")
            proyecto.retroceder(nombre)
        elif opcion == "8":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

# Ejecutar el menú
menu()
