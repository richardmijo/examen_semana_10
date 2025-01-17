class Tarea:
    def __init__(self, nombre, descripcion, estado="pendiente"):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado
        self.anterior = None
        self.siguiente = None

class ListaDobleTareas:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar_tarea_al_final(self, nombre, descripcion, estado="pendiente"):
        nueva_tarea = Tarea(nombre, descripcion, estado)
        if not self.cabeza:
            self.cabeza = nueva_tarea
            self.cola = nueva_tarea
        else:
            nueva_tarea.anterior = self.cola
            self.cola.siguiente = nueva_tarea
            self.cola = nueva_tarea

    def insertar_tarea_en_posicion(self, posicion, nombre, descripcion, estado="pendiente"):
        nueva_tarea = Tarea(nombre, descripcion, estado)
        if posicion == 0:  # Insertar al principio
            if not self.cabeza:
                self.cabeza = nueva_tarea
                self.cola = nueva_tarea
            else:
                nueva_tarea.siguiente = self.cabeza
                self.cabeza.anterior = nueva_tarea
                self.cabeza = nueva_tarea
        else:
            actual = self.cabeza
            indice = 0
            while actual and indice < posicion:
                anterior = actual
                actual = actual.siguiente
                indice += 1
            if actual:  # Insertar en el medio
                nueva_tarea.siguiente = actual
                nueva_tarea.anterior = anterior
                anterior.siguiente = nueva_tarea
                actual.anterior = nueva_tarea
            else:  # Insertar al final
                self.agregar_tarea_al_final(nombre, descripcion, estado)

    def eliminar_tarea(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                return
            actual = actual.siguiente

    def listar_tareas(self):
        tareas = []
        actual = self.cabeza
        while actual:
            tareas.append({
                "nombre": actual.nombre,
                "descripcion": actual.descripcion,
                "estado": actual.estado
            })
            actual = actual.siguiente
        return tareas

