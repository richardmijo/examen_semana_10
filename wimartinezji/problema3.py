class Nodo:
    def __init__(self, tarea):
        self.tarea = tarea
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.tamano = 0

    def agregar_tarea(self, tarea):
        nuevo_nodo = Nodo(tarea)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
        self.tamano += 1

    def insertar_tarea(self, tarea, posicion):
        if posicion < 0 or posicion > self.tamano:
            print("Posición inválida.")
            return
        nuevo_nodo = Nodo(tarea)
        if posicion == 0:
            nuevo_nodo.siguiente = self.cabeza
            if self.cabeza is not None:
                self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            for _ in range(posicion - 1):
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            if actual.siguiente is not None:
                actual.siguiente.anterior = nuevo_nodo
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
        self.tamano += 1

    def eliminar_tarea(self, tarea):
        if self.cabeza is None:
            print("No hay tareas en la lista.")
            return
        actual = self.cabeza
        while actual is not None:
            if actual.tarea == tarea:
                if actual.anterior is not None:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                if actual.siguiente is not None:
                    actual.siguiente.anterior = actual.anterior
                self.tamano -= 1
                print(f"Tarea '{tarea}' eliminada.")
                return
            actual = actual.siguiente
        print(f"Tarea '{tarea}' no encontrada.")

    def recorrer_tareas_avanzar(self):
        if self.cabeza is None:
            print("No hay tareas en la lista.")
            return
        actual = self.cabeza
        while actual is not None:
            print(actual.tarea)
            actual = actual.siguiente

    def recorrer_tareas_retroceder(self):
        if self.cabeza is None:
            print("No hay tareas en la lista.")
            return
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        while actual is not None:
            print(actual.tarea)
            actual = actual.anterior

# Función para interactuar con el usuario
def menu():
    lista_tareas = ListaDobleEnlazada()

    while True:
        print("\n--- Menú ---")
        print("1. Agregar tarea")
        print("2. Insertar tarea en posición específica")
        print("3. Ver tareas (avanzar)")
        print("4. Ver tareas (retroceder)")
        print("5. Eliminar tarea")
        print("6. Salir")
        
        opcion = input("Elige una opción (1/2/3/4/5/6): ")
        
        if opcion == "1":
            tarea = input("Ingresa la tarea que deseas agregar: ")
            lista_tareas.agregar_tarea(tarea)
        elif opcion == "2":
            tarea = input("Ingresa la tarea que deseas insertar: ")
            posicion = int(input("Ingresa la posición en la que deseas insertar la tarea: "))
            lista_tareas.insertar_tarea(tarea, posicion)
        elif opcion == "3":
            print("\nTareas del proyecto (avanzando):")
            lista_tareas.recorrer_tareas_avanzar()
        elif opcion == "4":
            print("\nTareas del proyecto (retrocediendo):")
            lista_tareas.recorrer_tareas_retroceder()
        elif opcion == "5":
            tarea = input("Ingresa la tarea que deseas eliminar: ")
            lista_tareas.eliminar_tarea(tarea)
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 6.")

# Ejecutar el menú
menu()
