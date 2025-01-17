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

    def agregar_tarea(self, tarea):
        """Agregar una tarea al proyecto, manteniendo la lista circular"""
        if not self.tareas:
            self.tareas = tarea
            tarea.siguiente = tarea  
        else:
            tarea_actual = self.tareas
            while tarea_actual.siguiente != self.tareas:
                tarea_actual = tarea_actual.siguiente
            tarea_actual.siguiente = tarea
            tarea.siguiente = self.tareas  

    def eliminar_tarea(self, nombre_tarea):
        """Eliminar una tarea de la lista circular"""
        if not self.tareas:
            return False  
        
        tarea_actual = self.tareas
    
        if tarea_actual.nombre == nombre_tarea:
            
            while tarea_actual.siguiente != self.tareas:
                tarea_actual = tarea_actual.siguiente
            if tarea_actual == self.tareas:
                self.tareas = None  
            else:
                tarea_actual.siguiente = self.tareas.siguiente
                self.tareas = self.tareas.siguiente
            return True

        while tarea_actual.siguiente != self.tareas:
            if tarea_actual.siguiente.nombre == nombre_tarea:
                tarea_actual.siguiente = tarea_actual.siguiente.siguiente
                return True
            tarea_actual = tarea_actual.siguiente
        return False

    def recorrer_tareas_circular(self):
        """Recorrer las tareas de forma cíclica e imprimir cada una"""
        if not self.tareas:
            print("No hay tareas en este proyecto.")
            return
        
        tarea_actual = self.tareas
        while True:
            print(f"Tarea: {tarea_actual.nombre} - Estado: {tarea_actual.estado}")
            tarea_actual = tarea_actual.siguiente
            if tarea_actual == self.tareas:
                break

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
            proyectos_info.append(f"Proyecto {proyecto_actual.id_proyecto}: {proyecto_actual.nombre}")
            proyecto_actual = proyecto_actual.siguiente
        return proyectos_info


def mostrar_menu():
    print("\n--- Sistema de Administración de Proyectos con Listas Circulares ---")
    print("1. Agregar un nuevo proyecto")
    print("2. Agregar tarea a un proyecto")
    print("3. Eliminar tarea de un proyecto")
    print("4. Recorrer las tareas cíclicamente")
    print("5. Listar todos los proyectos")
    print("6. Salir")
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
        
        elif opcion == "4":
            id_proyecto = input("Ingrese el ID del proyecto para recorrer sus tareas: ")
            proyecto_actual = sistema.proyectos
            while proyecto_actual:
                if proyecto_actual.id_proyecto == id_proyecto:
                    print(f"Recorriendo las tareas del proyecto '{proyecto_actual.nombre}':")
                    proyecto_actual.recorrer_tareas_circular()
                    break
                proyecto_actual = proyecto_actual.siguiente
            else:
                print("No se encontró un proyecto con ese ID.")
        
        elif opcion == "5":
            proyectos_info = sistema.listar_proyectos()
            if proyectos_info:
                for info in proyectos_info:
                    print(info)
            else:
                print("No hay proyectos disponibles.")
        
        elif opcion == "6":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    main()
