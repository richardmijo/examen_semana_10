class Nodo:
    def __init__(self, tarea):
        self.tarea = tarea
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.cabeza = None
        self.size = 0

    def agregar_tarea(self, tarea):
        nuevo_nodo = Nodo(tarea)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cabeza.siguiente = self.cabeza  # Apunta a sí mismo para hacer circular
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
        self.size += 1

    def recorrer_tareas(self):
        if self.cabeza is None:
            print("No hay tareas en la lista.")
            return
        actual = self.cabeza
        while True:
            print(actual.tarea)
            actual = actual.siguiente
            if actual == self.cabeza:
                break

    def eliminar_tarea(self, tarea):
        if self.cabeza is None:
            print("No hay tareas en la lista.")
            return
        actual = self.cabeza
        previo = None
        while True:
            if actual.tarea == tarea:
                if previo is None:  # Eliminar la cabeza
                    if self.cabeza.siguiente == self.cabeza:  # Si es el único nodo
                        self.cabeza = None
                    else:
                        # Buscar el último nodo para redirigir su siguiente al siguiente de la cabeza
                        ultimo = self.cabeza
                        while ultimo.siguiente != self.cabeza:
                            ultimo = ultimo.siguiente
                        self.cabeza = self.cabeza.siguiente
                        ultimo.siguiente = self.cabeza
                else:
                    previo.siguiente = actual.siguiente
                self.size -= 1
                print(f"Tarea '{tarea}' eliminada.")
                return
            previo = actual
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        print(f"Tarea '{tarea}' no encontrada.")

# Función para interactuar con el usuario
def menu():
    lista_tareas = ListaCircular()

    while True:
        print("\n--- Menú ---")
        print("1. Agregar tarea")
        print("2. Ver tareas (cíclicamente)")
        print("3. Eliminar tarea")
        print("4. Salir")
        
        opcion = input("Elige una opción (1/2/3/4): ")
        
        if opcion == "1":
            tarea = input("Ingresa la tarea que deseas agregar: ")
            lista_tareas.agregar_tarea(tarea)
        elif opcion == "2":
            print("\nTareas del proyecto (cíclicas):")
            lista_tareas.recorrer_tareas()
        elif opcion == "3":
            tarea = input("Ingresa la tarea que deseas eliminar: ")
            lista_tareas.eliminar_tarea(tarea)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 4.")

# Ejecutar el menú
menu()
