class Tarea:
    def __init__(self, nombre, descripcion, estado):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado

    def __str__(self):
        return f"Tarea: {self.nombre}, Descripcion: {self.descripcion}, Estado: {self.estado}"


class Nodo:
    def __init__(self, tarea=None):
        self.tarea = tarea
        self.siguiente = None


class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def agregar_tarea(self, tarea):
        nuevo_nodo = Nodo(tarea)
        if not self.cabeza:
            # Si la lista esta vacia, el nodo apunta a si mismo
            self.cabeza = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
        else:
            # Encuentra el ultimo nodo y lo enlaza con el nuevo nodo
            temp = self.cabeza
            while temp.siguiente != self.cabeza:
                temp = temp.siguiente
            temp.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza

    def recorrer_circular(self):
        if not self.cabeza:
            print("No hay tareas en el proyecto.")
            return
        temp = self.cabeza
        while True:
            print(temp.tarea)
            temp = temp.siguiente
            if temp == self.cabeza:
                break

    def eliminar_tarea(self, nombre_tarea):
        if not self.cabeza:
            print("No hay tareas en el proyecto.")
            return
        
        temp = self.cabeza
        anterior = None
        while True:
            if temp.tarea.nombre == nombre_tarea:
                if anterior:
                    anterior.siguiente = temp.siguiente
                else:
                    # Si la tarea a eliminar es la cabeza, se debe mover la cabeza
                    if temp.siguiente == self.cabeza:  # Si solo hay una tarea
                        self.cabeza = None
                    else:
                        # Encontramos el ultimo nodo y actualizamos el puntero
                        ultimo = self.cabeza
                        while ultimo.siguiente != self.cabeza:
                            ultimo = ultimo.siguiente
                        self.cabeza = temp.siguiente
                        ultimo.siguiente = self.cabeza
                print(f"Tarea '{nombre_tarea}' eliminada con exito.")
                return
            anterior = temp
            temp = temp.siguiente
            if temp == self.cabeza:
                break
        print(f"Tarea '{nombre_tarea}' no encontrada.")


# Funcion principal que interactua con el usuario a traves de la consola
def main():
    lista_tareas = ListaCircular()
    
    while True:
        print("\nOpciones:")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Eliminar tarea")
        print("4. Salir")
        
        opcion = input("Elige una opción (1-4): ")
        
        if opcion == "1":
            nombre = input("Nombre de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            estado = input("Estado de la tarea (pendiente, en progreso, completada): ")
            tarea = Tarea(nombre, descripcion, estado)
            lista_tareas.agregar_tarea(tarea)
            print(f"Tarea '{nombre}' agregada.")
        
        elif opcion == "2":
            print("\nTareas en el proyecto:")
            lista_tareas.recorrer_circular()
        
        elif opcion == "3":
            nombre_tarea = input("Nombre de la tarea a eliminar: ")
            lista_tareas.eliminar_tarea(nombre_tarea)
        
        elif opcion == "4":
            print("Saliendo...")
            break
        
        else:
            print("Opcion no valida, por favor elige una opcion entre 1 y 4.")

# Llamada a la funcion principal
if __name__ == "__main__":
    main()
