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
    
    # Recorrer la lista hacia adelante
    def recorrer_adelante(self):
        if self.cabeza is None:
            print("La lista está vacía.")
            return
        actual = self.cabeza
        while actual is not None:
            print(f"Tarea: {actual.tarea.nombre}, Descripción: {actual.tarea.descripcion}, Estado: {actual.tarea.estado}")
            actual = actual.siguiente

    # Función recursiva para generar tareas
    def generar_tareas_recursivas(self, id_actual, id_final, descripcion_base):
        if id_actual > id_final:
            return  # Caso base: cuando el ID actual supera el ID final, se termina la recursión

        # Crear tarea con el nombre y la descripción base
        nombre_tarea = f"Tarea {id_actual}"
        estado_tarea = "pendiente"  # Podemos cambiar el estado si es necesario
        tarea = Tarea(nombre_tarea, descripcion_base, estado_tarea)

        # Insertar tarea en la lista
        self.insertar_final(tarea)

        # Llamada recursiva para generar la siguiente tarea
        self.generar_tareas_recursivas(id_actual + 1, id_final, descripcion_base)

# Función principal para interactuar con el usuario
def main():
    lista_tareas = ListaDobleEnlazada()
    
    # Solicitar el rango de IDs y la descripción base de la tarea
    id_inicio = int(input("Ingresa el ID de inicio: "))
    id_final = int(input("Ingresa el ID final: "))
    descripcion_base = input("Ingresa la descripción base para las tareas: ")
    
    # Generar las tareas de forma recursiva
    lista_tareas.generar_tareas_recursivas(id_inicio, id_final, descripcion_base)
    
    # Mostrar las tareas generadas
    print("\nTareas generadas:")
    lista_tareas.recorrer_adelante()

if __name__ == "__main__":
    main()
