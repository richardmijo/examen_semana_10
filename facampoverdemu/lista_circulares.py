class Tarea:
    def __init__(self, nombre, descripcion, estado="pendiente"):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado
        self.siguiente = None

class ListaCircularTareas:
    def __init__(self):
        self.cabeza = None

    def agregar_tarea(self, nombre, descripcion, estado="pendiente"):
        nueva_tarea = Tarea(nombre, descripcion, estado)
        if not self.cabeza:
            self.cabeza = nueva_tarea
            self.cabeza.siguiente = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nueva_tarea
            nueva_tarea.siguiente = self.cabeza

    def eliminar_tarea(self, nombre):
        if not self.cabeza:
            return
        actual = self.cabeza
        anterior = None
        while True:
            if actual.nombre == nombre:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    # Si eliminamos la cabeza, debemos buscar el último nodo para corregir el enlace
                    ultimo = self.cabeza
                    while ultimo.siguiente != self.cabeza:
                        ultimo = ultimo.siguiente
                    self.cabeza = self.cabeza.siguiente
                    ultimo.siguiente = self.cabeza
                if actual == self.cabeza and actual.siguiente == self.cabeza:
                    self.cabeza = None  # Si era el único elemento, la lista queda vacía
                return
            anterior = actual
            actual = actual.siguiente
            if actual == self.cabeza:
                break

    def recorrer_tareas(self, cantidad_ciclos=1):
        if not self.cabeza:
            return []
        actual = self.cabeza
        resultado = []
        for _ in range(cantidad_ciclos):
            while True:
                resultado.append({
                    "nombre": actual.nombre,
                    "descripcion": actual.descripcion,
                    "estado": actual.estado
                })
                actual = actual.siguiente
                if actual == self.cabeza:
                    break
        return resultado
