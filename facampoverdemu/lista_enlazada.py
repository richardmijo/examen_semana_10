class Tarea:
    def __init__(self, nombre, descripcion, estado="pendiente"):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado
        self.siguiente = None

class ListaTareas:
    def __init__(self):
        self.cabeza = None

    def agregar_tarea(self, nombre, descripcion, estado="pendiente"):
        nueva_tarea = Tarea(nombre, descripcion, estado)
        if not self.cabeza:
            self.cabeza = nueva_tarea
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva_tarea

    def cambiar_estado(self, nombre_tarea, nuevo_estado):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre_tarea:
                actual.estado = nuevo_estado
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

class Proyecto:
    def __init__(self, id_proyecto, nombre):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.tareas = ListaTareas()
        self.siguiente = None

class ListaProyectos:
    def __init__(self):
        self.cabeza = None

    def agregar_proyecto(self, id_proyecto, nombre):
        nuevo_proyecto = Proyecto(id_proyecto, nombre)
        if not self.cabeza:
            self.cabeza = nuevo_proyecto
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_proyecto

    def agregar_tarea_a_proyecto(self, id_proyecto, nombre_tarea, descripcion, estado="pendiente"):
        actual = self.cabeza
        while actual:
            if actual.id_proyecto == id_proyecto:
                actual.tareas.agregar_tarea(nombre_tarea, descripcion, estado)
                return
            actual = actual.siguiente

    def cambiar_estado_tarea(self, id_proyecto, nombre_tarea, nuevo_estado):
        actual = self.cabeza
        while actual:
            if actual.id_proyecto == id_proyecto:
                actual.tareas.cambiar_estado(nombre_tarea, nuevo_estado)
                return
            actual = actual.siguiente

    def listar_proyectos(self):
        proyectos = []
        actual = self.cabeza
        while actual:
            proyectos.append({
                "id": actual.id_proyecto,
                "nombre": actual.nombre,
                "tareas": actual.tareas.listar_tareas()
            })
            actual = actual.siguiente
        return proyectos

if __name__ == "__main__":
    lista_proyectos = ListaProyectos()
    lista_proyectos.agregar_proyecto(1, "Proyecto A")
    lista_proyectos.agregar_tarea_a_proyecto(1, "Tarea 1", "Descripcion de Tarea 1")
    lista_proyectos.agregar_tarea_a_proyecto(1, "Tarea 2", "Descripcion de Tarea 2", "en progreso")
    lista_proyectos.cambiar_estado_tarea(1, "Tarea 1", "completada")
    lista_proyectos.agregar_proyecto(2, "Proyecto B")
    lista_proyectos.agregar_tarea_a_proyecto(2, "Tarea 3", "Descripcion de Tarea 3")

    print("Proyectos y sus tareas:")
    for proyecto in lista_proyectos.listar_proyectos():
        print(f"Proyecto: {proyecto['nombre']} (ID: {proyecto['id']})")
        for tarea in proyecto['tareas']:
            print(f"  - Tarea: {tarea['nombre']}, Estado: {tarea['estado']}, Descripcion: {tarea['descripcion']}")
