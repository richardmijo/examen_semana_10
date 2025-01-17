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
            self._agregar_tarea_recursivo(self.cabeza, nuevo_nodo)
        self.tamano += 1

    def _agregar_tarea_recursivo(self, nodo_actual, nuevo_nodo):
        if nodo_actual.siguiente is None:
            nodo_actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nodo_actual
        else:
            self._agregar_tarea_recursivo(nodo_actual.siguiente, nuevo_nodo)

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
            self._insertar_tarea_recursivo(self.cabeza, nuevo_nodo, 0, posicion)
        self.tamano += 1

    def _insertar_tarea_recursivo(self, nodo_actual, nuevo_nodo, contador, posicion):
        if contador == posicion - 1:
            nuevo_nodo.siguiente = nodo_actual.siguiente
            if nodo_actual.siguiente is not None:
                nodo_actual.siguiente.anterior = nuevo_nodo
            nodo_actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nodo_actual
        else:
            self._insertar_tarea_recursivo(nodo_actual.siguiente, nuevo_nodo, contador + 1, posicion)

    def eliminar_tarea(self, tarea):
        if self.cabeza is None:
            print("No hay tareas en la lista.")
            return
        self._eliminar_tarea_recursivo(self.cabeza, tarea)

    def _eliminar_tarea_recursivo(self, nodo_actual, tarea):
        if nodo_actual is None:
            print(f"Tarea '{tarea}' no encontrada.")
            return
        if nodo_actual.tarea == tarea:
            if nodo_actual.anterior is not None:
                nodo_actual.anterior.siguiente = nodo_actual.siguiente
            else:
                self.cabeza = nodo_actual.siguiente
            if nodo_actual.siguiente is not None:
                nodo_actual.siguiente.anterior = nodo_actual.anterior
            self.tamano -= 1
            print(f"Tarea '{tarea}' eliminada.")
        else:
            self._eliminar_tarea_recursivo(nodo_actual.siguiente, tarea)

    def recorrer_tareas_avanzar(self):
        if self.cabeza is None:
            print("No hay tareas en la lista.")
            return
        self._recorrer_tareas_avanzar_recursivo(self.cabeza)

    def _recorrer_tareas_avanzar_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            print(nodo_actual.tarea)
            self._recorrer_tareas_avanzar_recursivo(nodo_actual.siguiente)

    def recorrer_tareas_retroceder(self):
        if self.cabeza is None:
            print("No hay tareas en la lista.")
            return
        # Ir al final de la lista para empezar el recorrido hacia atrás
        self._recorrer_tareas_retroceder_recursivo(self.cabeza)

    def _recorrer_tareas_retroceder_recursivo(self, nodo_actual):
        if nodo_actual.siguiente is not None:
            self._recorrer_tareas_retroceder_recursivo(nodo_actual.siguiente)
        print(nodo_actual.tarea)

    def generar_tareas_recursivas(self, inicio, fin, descripcion_base):
        if inicio > fin:
            return
        tarea = f"{descripcion_base} {inicio}"
        self.agregar_tarea(tarea)
        self.generar_tareas_recursivas(inicio + 1, fin, descripcion_base)

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
        print("6. Generar tareas automáticamente")
        print("7. Salir")
        
        opcion = input("Elige una opción (1/2/3/4/5/6/7): ")
        
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
            inicio = int(input("Ingresa el ID de inicio: "))
            fin = int(input("Ingresa el ID de fin: "))
            descripcion_base = input("Ingresa la descripción base de las tareas: ")
            lista_tareas.generar_tareas_recursivas(inicio, fin, descripcion_base)
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 7.")

# Ejecutar el menú
menu()
