class Nodo:
    def __init__(self, id_tarea, descripcion):
        self.id_tarea = id_tarea
        self.descripcion = descripcion
        self.anterior = None
        self.siguiente = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar(self, id_tarea, descripcion):
        nuevo_nodo = Nodo(id_tarea, descripcion)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo

    def mostrar_recursivo(self, nodo):
        if nodo is None:
            return
        print(f"ID: {nodo.id_tarea}, Descripción: {nodo.descripcion}")
        self.mostrar_recursivo(nodo.siguiente)

    def mostrar(self):
        self.mostrar_recursivo(self.cabeza)


def generar_tareas(lista, id_inicio, id_fin, descripcion_base):
    # Caso base: si el rango se ha completado
    if id_inicio > id_fin:
        return
    lista.insertar(id_inicio, f"{descripcion_base} {id_inicio}")
    generar_tareas(lista, id_inicio + 1, id_fin, descripcion_base)
