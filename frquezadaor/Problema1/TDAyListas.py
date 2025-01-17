class Tarea:
    def __init__(self, nombre, descripcion, estado='pendiente'):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado
        self.siguiente = None  

class Proyecto:
    def __init__(self, id_proyecto, nombre):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.tareas = None  
        self.siguiente = None  

    def agregar_tarea(self, tarea):
        """Agregar una tarea al proyecto"""
        if not self.tareas:
            self.tareas = tarea
        else:
            tarea_actual = self.tareas
            while tarea_actual.siguiente:
                tarea_actual = tarea_actual.siguiente
            tarea_actual.siguiente = tarea

    def cambiar_estado_tarea(self, nombre_tarea, nuevo_estado):
        """Cambiar el estado de una tarea"""
        tarea_actual = self.tareas
        while tarea_actual:
            if tarea_actual.nombre == nombre_tarea:
                tarea_actual.estado = nuevo_estado
                return True
            tarea_actual = tarea_actual.siguiente
        return False

    def listar_tareas(self):
        """Listar todas las tareas con su estado"""
        tareas = []
        tarea_actual = self.tareas
        while tarea_actual:
            tareas.append(f"{tarea_actual.nombre} - {tarea_actual.estado}")
            tarea_actual = tarea_actual.siguiente
        return tareas

class SistemaProyectos:
    def __init__(self):
        self.proyectos = None  

    def agregar_proyecto(self, proyecto):
        """Agregar un nuevo proyecto al sistema"""
        if not self.proyectos:
            self.proyectos = proyecto
        else:
            proyecto_actual = self.proyectos
            while proyecto_actual.siguiente:
                proyecto_actual = proyecto_actual.siguiente
            proyecto_actual.siguiente = proyecto

    def listar_proyectos(self):
        """Listar todos los proyectos y sus tareas"""
        proyectos_info = []
        proyecto_actual = self.proyectos
        while proyecto_actual:
            tareas_info = proyecto_actual.listar_tareas()
            proyectos_info.append(f"Proyecto {proyecto_actual.id_proyecto}: {proyecto_actual.nombre} - Tareas: {', '.join(tareas_info)}")
            proyecto_actual = proyecto_actual.siguiente
        return proyectos_info

def mostrar_menu():
    print("\n--- Sistema de Administración de Proyectos ---")
    print("1. Agregar un nuevo proyecto")
    print("2. Agregar tarea a un proyecto")
    print("3. Cambiar el estado de una tarea")
    print("4. Listar todos los proyectos y sus tareas")
    print("5. Salir")
    return input("Elige una opción: ")

def main():
    sistema = SistemaProyectos()
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
           
            nombre_proyecto = input("Ingrese el nombre del proyecto: ")
            id_proyecto = input("Ingrese el ID unico del proyecto: ")
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
            proyecto_actual = sistema.proyectos
            while proyecto_actual:
                if proyecto_actual.id_proyecto == id_proyecto:
                    nombre_tarea = input("Ingrese el nombre de la tarea a cambiar el estado: ")
                    nuevo_estado = input("Ingrese el nuevo estado (pendiente, en progreso, completada): ")
                    if proyecto_actual.cambiar_estado_tarea(nombre_tarea, nuevo_estado):
                        print(f"El estado de la tarea '{nombre_tarea}' se ha cambiado a '{nuevo_estado}'.")
                    else:
                        print("No se encontró una tarea con ese nombre.")
                    break
                proyecto_actual = proyecto_actual.siguiente
            else:
                print("No se encontró un proyecto con ese ID.")
        
        elif opcion == "4":
            proyectos_info = sistema.listar_proyectos()
            if proyectos_info:
                for info in proyectos_info:
                    print(info)
            else:
                print("No hay proyectos disponibles.")
        
        elif opcion == "5":
            print("Saliendo de la aplicacion")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
