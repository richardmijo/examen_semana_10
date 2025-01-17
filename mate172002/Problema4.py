class NodoTarea:
    def __init__(self, nombre, estado="pendiente"):
        self.nombre = nombre
        self.estado = estado
        self.anterior = None
        self.siguiente = None

class ListaTareasDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar_tarea(self, nombre, estado="pendiente"):
        nueva_tarea = NodoTarea(nombre, estado)
        if not self.cabeza:
            self.cabeza = self.cola = nueva_tarea
        else:
            self.cola.siguiente = nueva_tarea
            nueva_tarea.anterior = self.cola
            self.cola = nueva_tarea

    def insertar_tarea(self, posicion, nombre, estado="pendiente"):
        nueva_tarea = NodoTarea(nombre, estado)
        if posicion == 0:
            if not self.cabeza:
                self.cabeza = self.cola = nueva_tarea
            else:
                nueva_tarea.siguiente = self.cabeza
                self.cabeza.anterior = nueva_tarea
                self.cabeza = nueva_tarea
        else:
            actual = self.cabeza
            index = 0
            while actual and index < posicion:
                index += 1
                actual = actual.siguiente

            if actual:
                previa = actual.anterior
                previa.siguiente = nueva_tarea
                nueva_tarea.anterior = previa
                nueva_tarea.siguiente = actual
                actual.anterior = nueva_tarea
            else:
                self.agregar_tarea(nombre, estado)

    def eliminar_tarea(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre:
                if actual == self.cabeza:
                    self.cabeza = actual.siguiente
                    if self.cabeza:
                        self.cabeza.anterior = None
                elif actual == self.cola:
                    self.cola = actual.anterior
                    self.cola.siguiente = None
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                return True
            actual = actual.siguiente
        return False

    def avanzar(self):
        if self.cabeza:
            actual = self.cabeza
            while actual:
                print(f"Tarea: {actual.nombre}, Estado: {actual.estado}")
                actual = actual.siguiente

    def retroceder(self):
        if self.cola:
            actual = self.cola
            while actual:
                print(f"Tarea: {actual.nombre}, Estado: {actual.estado}")
                actual = actual.anterior

    def generar_tareas_recursivo(self, inicio, fin, descripcion_base):
        if inicio > fin:
            return
        self.agregar_tarea(f"{descripcion_base} {inicio}")
        self.generar_tareas_recursivo(inicio + 1, fin, descripcion_base)

lista_tareas = ListaTareasDoblementeEnlazada()
lista_tareas.generar_tareas_recursivo(1, 5, "Tarea")


print("Avanzando:")
lista_tareas.avanzar()
