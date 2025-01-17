class Tarea:
    def __init__(self, nombre, descripcion, estado='pendiente'):
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

    def agregar_tarea(self, tarea):
        if not self.tareas:
            self.tareas = tarea
        else:
            tarea_actual = self.tareas
            while tarea_actual.siguiente:
                tarea_actual = tarea_actual.siguiente
            tarea_actual.siguiente = tarea
            tarea.anterior = tarea_actual

    def insertar_tarea(self, tarea, posicion):
        if posicion == 0:
            tarea.siguiente = self.tareas
            if self.tareas:
                self.tareas.anterior = tarea
            self.tareas = tarea
            tarea.anterior = None
        else:
            tarea_actual = self.tareas
            indice = 0
            while tarea_actual and indice < posicion:
                tarea_actual = tarea_actual.siguiente
                indice += 1

            if tarea_actual:
                tarea.siguiente = tarea_actual
                tarea.anterior = tarea_actual.anterior
                if tarea_actual.anterior:
                    tarea_actual.anterior.siguiente = tarea
                tarea_actual.anterior = tarea
            else:
                self.agregar_tarea(tarea)

    def eliminar_tarea(self, nombre_tarea):
        tarea_actual = self.tareas
        while tarea_actual:
            if tarea_actual.nombre == nombre_tarea:
                if tarea_actual.anterior:
                    tarea_actual.anterior.siguiente = tarea_actual.siguiente
                if tarea_actual.siguiente:
                    tarea_actual.siguiente.anterior = tarea_actual.anterior
                if tarea_actual == self.tareas:
                    self.tareas = tarea_actual.siguiente
                return True
            tarea_actual = tarea_actual.siguiente
        return False

    def recorrer_tareas(self):
        tareas = []
        tarea_actual = self.tareas
        while tarea_actual:
            tareas.append(f"{tarea_actual.nombre} - {tarea_actual.estado}")
            tarea_actual = tarea_actual.siguiente
        return tareas

    def recorrer_tareas_reversa(self):
        tareas = []
        tarea_actual = self.tareas
        while tarea_actual and tarea_actual.siguiente:
            tarea_actual = tarea_actual.siguiente
        while tarea_actual:
            tareas.append(f"{tarea_actual.nombre} - {tarea_actual.estado}")
            tarea_actual = tarea_actual.anterior
        return tareas

class SistemaProyectos:
    def __init__(self):
        self.proyectos = None

    def agregar_proyecto(self, proyecto):
        if not self.proyectos:
            self.proyectos = proyecto
        else:
            proyecto_actual = self.proyectos
            while proyecto_actual.siguiente:
                proyecto_actual = proyecto_actual.siguiente
            proyecto_actual.siguiente = proyecto

    def listar_proyectos(self):
        proyectos_info = []
        proyecto_actual = self.proyectos
        while proyecto_actual:
            proyectos_info.append(f"Proyecto {proyecto_actual.id_proyecto}: {proyecto_actual.nombre}")
            proyecto_actual = proyecto_actual.siguiente
        return proyectos_info

def mostrar_menu():
    print("\n--- Sistema de Administración de Proyectos con Listas Doblemente Enlazadas ---")
    print("1. Agregar un nuevo proyecto")
    print("2. Agregar tarea a un proyecto")
    print("3. Insertar tarea en una posición específica")
    print("4. Eliminar tarea de un proyecto")
    print("5. Recorrer las tareas (adelante)")
    print("6. Recorrer las tareas (reversa)")
    print("7. Listar todos los proyectos")
    print("8. Salir")
    return input("Elige una opción: ")

def main():
    sistema = SistemaProyectos()
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            nombre_proyecto = input("Ingrese el nombre del proyecto: ")
            id_proyecto = input("Ingrese el ID único del proyecto: ")
            proyecto = Proyecto(id_proyecto, nombre_proyecto)
            sistema.agregar_proyecto(proyecto)
            print(f"Proyecto '{nombre_proyecto}' agregado con éxito.")

        elif opcion == "2":
            id_proyecto = input("Ingrese el ID del proyecto al que desea agregar la tarea: ")
            proyecto_actual = sistema.proyectos
            while proyecto_actual:
                if proyecto_actual.id_proyecto == id_proyecto:
                    nombre_tarea = input("Ingrese el nombre de la tarea: ")
                    descripcion_tarea = input("Ingrese la descripción de la tarea: ")
                    tarea = Tarea(nombre_tarea, descripcion_tarea)
                    proyecto_actual.agregar_tarea(tarea)
                    print(f"Tarea '{nombre_tarea}' agregada al proyecto '{proyecto_actual.nombre}'.")
                    break
                proyecto_actual = proyecto_actual.siguiente
            else:
                print("No se encontró un proyecto con ese ID.")

        elif opcion == "3":
            id_proyecto = input("Ingrese el ID del proyecto: ")
            nombre_tarea = input("Ingrese el nombre de la tarea: ")
            descripcion_tarea = input("Ingrese la descripción de la tarea: ")
            posicion = int(input("Ingrese la posición en la que desea insertar la tarea: "))
            proyecto_actual = sistema.proyectos
            while proyecto_actual:
                if proyecto_actual.id_proyecto == id_proyecto:
                    tarea = Tarea(nombre_tarea, descripcion_tarea)
                    proyecto_actual.insertar_tarea(tarea, posicion)
                    print(f"Tarea '{nombre_tarea}' insertada en la posición {posicion} del proyecto '{proyecto_actual.nombre}'.")
                    break
                proyecto_actual = proyecto_actual.siguiente
            else:
                print("No se encontró un proyecto con ese ID.")

        elif opcion == "4":
            id_proyecto = input("Ingrese el ID del proyecto: ")
            nombre_tarea = input("Ingrese el nombre de la tarea a eliminar: ")
            proyecto_actual = sistema.proyectos
            while proyecto_actual:
                if proyecto_actual.id_proyecto == id_proyecto:
                    if proyecto_actual.eliminar_tarea(nombre_tarea):
                        print(f"Tarea '{nombre_tarea}' eliminada del proyecto '{proyecto_actual.nombre}'.")
                    else:
                        print("No se encontró una tarea con ese nombre.")
                    break
                proyecto_actual = proyecto_actual.siguiente
            else:
                print("No se encontró un proyecto con ese ID.")

        elif opcion == "5":
            id_proyecto = input("Ingrese el ID del proyecto para recorrer sus tareas: ")
            proyecto_actual = sistema.proyectos
            while proyecto_actual:
                if proyecto_actual.id_proyecto == id_proyecto:
                    print(f"Tareas del proyecto '{proyecto_actual.nombre}':")
                    tareas_info = proyecto_actual.recorrer_tareas()
                    for tarea in tareas_info:
                        print(tarea)
                    break
                proyecto_actual = proyecto_actual.siguiente
            else:
                print("No se encontró un proyecto con ese ID.")

        elif opcion == "6":
            id_proyecto = input("Ingrese el ID del proyecto para recorrer sus tareas en reversa: ")
            proyecto_actual = sistema.proyectos
            while proyecto_actual:
                if proyecto_actual.id_proyecto == id_proyecto:
                    print(f"Tareas del proyecto '{proyecto_actual.nombre}' en reversa:")
                    tareas_info = proyecto_actual.recorrer_tareas_reversa()
                    for tarea in tareas_info:
                        print(tarea)
                    break
                proyecto_actual = proyecto_actual.siguiente
            else:
                print("No se encontró un proyecto con ese ID.")

        elif opcion == "7":
            proyectos_info = sistema.listar_proyectos()
            if proyectos_info:
                for info in proyectos_info:
                    print(info)
            else:
                print("No hay proyectos disponibles.")

        elif opcion == "8":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    main()
