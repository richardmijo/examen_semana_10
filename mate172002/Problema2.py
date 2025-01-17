class NodoTarea:
    def __init__(self, nombre, estado="pendiente"):
        self.nombre = nombre
        self.estado = estado
        self.siguiente = None

class ListaTareasCircular:
    def __init__(self):
        self.cabeza = None

    def agregar_tarea(self, nombre, estado="pendiente"):
        nueva_tarea = NodoTarea(nombre, estado)
        if not self.cabeza:
            self.cabeza = nueva_tarea
            nueva_tarea.siguiente = self.cabeza  
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nueva_tarea
            nueva_tarea.siguiente = self.cabeza

    def recorrer_circular(self, vueltas=1):
        if not self.cabeza:
            print("No hay tareas.")
            return

        actual = self.cabeza
        contador = 0
        while contador < vueltas:
            print(f"Tarea: {actual.nombre}, Estado: {actual.estado}")
            actual = actual.siguiente
            if actual == self.cabeza:
                contador += 1


lista_tareas = ListaTareasCircular()
lista_tareas.agregar_tarea("Diseñar interfaz")
lista_tareas.agregar_tarea("Implementar backend")

print("Tareas en lista circular:")
lista_tareas.recorrer_circular(vueltas=2)
