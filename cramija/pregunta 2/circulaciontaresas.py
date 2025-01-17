class Tarea:
    def __init__(self, nombre, descripcion, estado="pendiente"):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.inicio = None

    def agregar_tarea(self, nombre, descripcion):
        nueva_tarea = Tarea(nombre, descripcion)
        if not self.inicio:
            self.inicio = nueva_tarea
            self.inicio.siguiente = self.inicio
        else:
            actual = self.inicio
            while actual.siguiente != self.inicio:
                actual = actual.siguiente
            actual.siguiente = nueva_tarea
            nueva_tarea.siguiente = self.inicio

    def listar_tareas_circular(self):
        if not self.inicio:
            print("No hay tareas en la lista.")
            return
        actual = self.inicio
        while True:
            print(f"Tarea: {actual.nombre}, Descripción: {actual.descripcion}, Estado: {actual.estado}")
            actual = actual.siguiente
            if actual == self.inicio:
                break

    def eliminar_tarea(self, nombre):
        if not self.inicio:
            print("No hay tareas para eliminar.")
            return
        actual = self.inicio
        anterior = None
        while True:
            if actual.nombre == nombre:
                if anterior:
                    anterior.siguiente = actual.siguiente
                if actual == self.inicio:
                    self.inicio = actual.siguiente if actual.siguiente != self.inicio else None
                print(f"Tarea '{nombre}' eliminada.")
                return
            anterior = actual
            actual = actual.siguiente
            if actual == self.inicio:
                break
        print(f"Tarea '{nombre}' no encontrada.")

# MENU

def menu_lista_circular():
    lista = ListaCircular()
    
    while True:
        print("\nMenú de Lista Circular")
        print("1. Agregar Tarea")
        print("2. Listar Tareas")
        print("3. Eliminar Tarea")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            lista.agregar_tarea(nombre, descripcion)
            print("Tarea agregada exitosamente.")
        
        elif opcion == "2":
            print("Listado de tareas:")
            lista.listar_tareas_circular()
        
        elif opcion == "3":
            nombre = input("Nombre de la tarea a eliminar: ")
            lista.eliminar_tarea(nombre)
        
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# MENU

menu_lista_circular()