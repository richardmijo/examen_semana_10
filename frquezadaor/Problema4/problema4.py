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

    def generar_tareas_recursivo(self, id_inicial, id_final, descripcion_base):
        if id_inicial > id_final:
            return
        nombre_tarea = f"Tarea {id_inicial}"
        descripcion_tarea = f"{descripcion_base} {id_inicial}"
        tarea = Tarea(nombre_tarea, descripcion_tarea)
        self.agregar_tarea(tarea)
        self.generar_tareas_recursivo(id_inicial + 1, id_final, descripcion_base)

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
    print("\n--- Sistema de Administración de Proyectos con Tareas Automáticas ---")
    print("1. Agregar un nuevo proyecto")
    print("2. Generar tareas automáticamente")
    print("3. Listar todos los proyectos")
    print("4. Salir")
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
            id_proyecto = input("Ingrese el ID del proyecto al que desea agregar las tareas: ")
            id_inicial = int(input("Ingrese el ID inicial de las tareas: "))
            id_final = int(input("Ingrese el ID final de las tareas: "))
            descripcion_base = input("Ingrese la descripción base de las tareas: ")
            proyecto_actual = sistema.proyectos
            while proyecto_actual:
                if proyecto_actual.id_proyecto == id_proyecto:
                    proyecto_actual.generar_tareas_recursivo(id_inicial, id_final, descripcion_base)
                    print(f"Tareas generadas del ID {id_inicial} al ID {id_final}.")
                    break
                proyecto_actual = proyecto_actual.siguiente
            else:
                print("No se encontró un proyecto con ese ID.")

        elif opcion == "3":
            proyectos_info = sistema.listar_proyectos()
            if proyectos_info:
                for info in proyectos_info:
                    print(info)
            else:
                print("No hay proyectos disponibles.")

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    main()
