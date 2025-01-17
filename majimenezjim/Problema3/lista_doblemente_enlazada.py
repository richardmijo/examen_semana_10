class Tarea:
    def __init__(self, nombre, descripcion, estado):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado

class Nodo:
    def __init__(self, tarea=None):
        self.tarea = tarea
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
    # Insertar una tarea al final de la lista
    def insertar_final(self, tarea):
        nuevo_nodo = Nodo(tarea)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
    
    # Insertar una tarea al principio de la lista
    def insertar_inicio(self, tarea):
        nuevo_nodo = Nodo(tarea)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
    
    # Insertar una tarea en una posición específica
    def insertar_en_posicion(self, tarea, posicion):
        if posicion == 0:
            self.insertar_inicio(tarea)
            return
        nuevo_nodo = Nodo(tarea)
        actual = self.cabeza
        cuenta = 0
        while actual is not None and cuenta < posicion:
            actual = actual.siguiente
            cuenta += 1
        if actual is None:  # Si la posición es mayor que el tamaño de la lista, la insertamos al final
            self.insertar_final(tarea)
        else:
            nuevo_nodo.siguiente = actual
            nuevo_nodo.anterior = actual.anterior
            if actual.anterior:
                actual.anterior.siguiente = nuevo_nodo
            actual.anterior = nuevo_nodo
    
    # Eliminar una tarea en una posición específica
    def eliminar_en_posicion(self, posicion):
        if self.cabeza is None:
            print("La lista está vacía.")
            return
        actual = self.cabeza
        cuenta = 0
        while actual is not None and cuenta < posicion:
            actual = actual.siguiente
            cuenta += 1
        if actual is None:  # No se encontró la tarea en la posición dada
            print("Posición fuera de rango.")
            return
        if actual.anterior:
            actual.anterior.siguiente = actual.siguiente
        if actual.siguiente:
            actual.siguiente.anterior = actual.anterior
        if actual == self.cabeza:  # Si es la cabeza, cambiamos la cabeza
            self.cabeza = actual.siguiente
        if actual == self.cola:  # Si es la cola, cambiamos la cola
            self.cola = actual.anterior
        del actual
    
    # Recorrer la lista hacia adelante
    def recorrer_adelante(self):
        if self.cabeza is None:
            print("La lista está vacía.")
            return
        actual = self.cabeza
        while actual is not None:
            print(f"Tarea: {actual.tarea.nombre}, Descripción: {actual.tarea.descripcion}, Estado: {actual.tarea.estado}")
            actual = actual.siguiente
    
    # Recorrer la lista hacia atrás
    def recorrer_atras(self):
        if self.cola is None:
            print("La lista está vacía.")
            return
        actual = self.cola
        while actual is not None:
            print(f"Tarea: {actual.tarea.nombre}, Descripción: {actual.tarea.descripcion}, Estado: {actual.tarea.estado}")
            actual = actual.anterior

# Función principal para interactuar con el usuario
def main():
    lista_tareas = ListaDobleEnlazada()

    while True:
        print("\nOpciones:")
        print("1. Agregar tarea al inicio")
        print("2. Agregar tarea al final")
        print("3. Insertar tarea en posición")
        print("4. Eliminar tarea en posición")
        print("5. Ver tareas (adelante)")
        print("6. Ver tareas (atrás)")
        print("7. Salir")
        
        opcion = input("Elige una opción (1-7): ")

        if opcion == "1":
            nombre = input("Nombre de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            estado = input("Estado de la tarea (pendiente, en progreso, completada): ")
            tarea = Tarea(nombre, descripcion, estado)
            lista_tareas.insertar_inicio(tarea)
        
        elif opcion == "2":
            nombre = input("Nombre de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            estado = input("Estado de la tarea (pendiente, en progreso, completada): ")
            tarea = Tarea(nombre, descripcion, estado)
            lista_tareas.insertar_final(tarea)
        
        elif opcion == "3":
            nombre = input("Nombre de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            estado = input("Estado de la tarea (pendiente, en progreso, completada): ")
            tarea = Tarea(nombre, descripcion, estado)
            posicion = int(input("Posición en la lista para insertar la tarea: "))
            lista_tareas.insertar_en_posicion(tarea, posicion)
        
        elif opcion == "4":
            posicion = int(input("Posición de la tarea a eliminar: "))
            lista_tareas.eliminar_en_posicion(posicion)
        
        elif opcion == "5":
            lista_tareas.recorrer_adelante()
        
        elif opcion == "6":
            lista_tareas.recorrer_atras()
        
        elif opcion == "7":
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 7.")

if __name__ == "__main__":
    main()
