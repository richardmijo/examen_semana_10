#
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
        return f"Tarea: {self.nombre} | Estado: {self.estado} | Descripción: {self.descripcion}"



class NodoTarea:
    def __init__(self, tarea):
        self.tarea = tarea
        self.siguiente = None


class Proyecto:
    def __init__(self, id_proyecto, nombre):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.tareas = None  

    def agregar_tarea(self, nombre_tarea, descripcion):
        nueva_tarea = NodoTarea(Tarea(nombre_tarea, descripcion))
        if self.tareas is None:
            self.tareas = nueva_tarea
            nueva_tarea.siguiente = nueva_tarea 
        else:
            actual = self.tareas
            while actual.siguiente != self.tareas:  
                actual = actual.siguiente
            actual.siguiente = nueva_tarea
            nueva_tarea.siguiente = self.tareas 

    def eliminar_tarea(self, nombre_tarea):
        if self.tareas is None:
            raise ValueError("No hay tareas en el proyecto.")
        
        actual = self.tareas
        anterior = None
        
        while actual.siguiente != self.tareas:  
            if actual.tarea.nombre == nombre_tarea:
                if anterior is None:  
                    ultimo = self.tareas
                    while ultimo.siguiente != self.tareas:
                        ultimo = ultimo.siguiente
                    self.tareas = actual.siguiente
                    ultimo.siguiente = self.tareas
                else:
                    anterior.siguiente = actual.siguiente
                print(f"Tarea '{nombre_tarea}' eliminada.")
                return
            anterior = actual
            actual = actual.siguiente

 
        if actual.tarea.nombre == nombre_tarea:
            if actual.siguiente == self.tareas: 
                self.tareas = None
            else:  
                anterior.siguiente = actual.siguiente
            print(f"Tarea '{nombre_tarea}' eliminada.")
        else:
            raise ValueError(f"Tarea '{nombre_tarea}' no encontrada en el proyecto.")

    def recorrer_tareas(self):
        if self.tareas is None:
            print("No hay tareas en este proyecto.")
            return

        actual = self.tareas
        while True:
            print(actual.tarea)
            actual = actual.siguiente
            if actual == self.tareas:
                break  



def menu():
    lista_proyectos = []

    while True:
        print("\n=== Sistema de Administración de Proyectos ===")
        print("1. Agregar un nuevo proyecto")
        print("2. Agregar tarea a un proyecto")
        print("3. Eliminar tarea de un proyecto")
        print("4. Recorrer tareas de un proyecto cíclicamente")
        print("5. Listar todos los proyectos y sus tareas")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_proyecto = input("Ingrese el ID del proyecto: ")
            nombre_proyecto = input("Ingrese el nombre del proyecto: ")
            lista_proyectos.append(Proyecto(id_proyecto, nombre_proyecto))
            print("Proyecto agregado con éxito.")
        
        elif opcion == '2':
            id_proyecto = input("Ingrese el ID del proyecto: ")
            nombre_tarea = input("Ingrese el nombre de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")

            proyecto = next((p for p in lista_proyectos if p.id_proyecto == id_proyecto), None)
            if proyecto:
                proyecto.agregar_tarea(nombre_tarea, descripcion)
                print("Tarea agregada con éxito.")
            else:
                print(f"No se encontró el proyecto con ID: {id_proyecto}")

        elif opcion == '3':
            id_proyecto = input("Ingrese el ID del proyecto: ")
            nombre_tarea = input("Ingrese el nombre de la tarea a eliminar: ")

            proyecto = next((p for p in lista_proyectos if p.id_proyecto == id_proyecto), None)
            if proyecto:
                try:
                    proyecto.eliminar_tarea(nombre_tarea)
                except ValueError as e:
                    print(e)
            else:
                print(f"No se encontró el proyecto con ID: {id_proyecto}")

        elif opcion == '4':
            id_proyecto = input("Ingrese el ID del proyecto: ")

            proyecto = next((p for p in lista_proyectos if p.id_proyecto == id_proyecto), None)
            if proyecto:
                proyecto.recorrer_tareas()
            else:
                print(f"No se encontró el proyecto con ID: {id_proyecto}")

        elif opcion == '5':
            for proyecto in lista_proyectos:
                print(f"Proyecto: {proyecto.nombre} (ID: {proyecto.id_proyecto})")
                proyecto.recorrer_tareas()

        elif opcion == '6':
            print("¡Gracias por usar el sistema!")
            break

        else:
            print("Opcion no . Intentelo nuevamente.")



menu()
