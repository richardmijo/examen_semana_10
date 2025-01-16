class Tarea:
    def __init__(self, nombre, descripcion, estado="pendiente"):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado
        self.siguiente = None

class Proyecto:
    def __init__(self, id_proyecto, nombre):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.tareas = None

    def agregar_tarea(self, nombre_tarea, descripcion):
        nueva_tarea = Tarea(nombre_tarea, descripcion)
        if not self.tareas:
            self.tareas = nueva_tarea
        else:
            actual = self.tareas
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva_tarea

    def listar_tareas(self):
        actual = self.tareas
        if not actual:
            print("No hay tareas en el proyecto.")
        else:
            while actual:
                print(f"Tarea: {actual.nombre}, Descripción: {actual.descripcion}, Estado: {actual.estado}")
                actual = actual.siguiente

    def cambiar_estado_tarea(self, nombre_tarea, nuevo_estado):
        actual = self.tareas
        while actual:
            if actual.nombre == nombre_tarea:
                actual.estado = nuevo_estado
                print(f"Estado de '{nombre_tarea}' cambiado a '{nuevo_estado}'.")
                return
            actual = actual.siguiente
        print(f"Tarea '{nombre_tarea}' no encontrada.")

# Menu
def menu_interactivo():
    proyecto = Proyecto(1, "Proyecto A")
    
    while True:
        print("\nMenú de Proyecto")
        print("1. Agregar Tarea")
        print("2. Listar Tareas")
        print("3. Cambiar Estado de una Tarea")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            nombre_tarea = input("Nombre de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            proyecto.agregar_tarea(nombre_tarea, descripcion)
            print("Tarea agregada exitosamente.")
        
        elif opcion == "2":
            print("Listado de tareas:")
            proyecto.listar_tareas()
        
        elif opcion == "3":
            nombre_tarea = input("Nombre de la tarea a cambiar estado: ")
            nuevo_estado = input("Nuevo estado: ")
            proyecto.cambiar_estado_tarea(nombre_tarea, nuevo_estado)
        
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# MENU



menu_interactivo()