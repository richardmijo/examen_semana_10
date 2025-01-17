class Nodo:
    def __init__(self, data):
        self.data = data  # Contiene el objeto (proyecto o tarea)
        self.next = None  # Referencia al siguiente nodo


class ListaEnlazada:
    def __init__(self):
        self.head = None  # Nodo inicial de la lista

    def agregar(self, data):
        nuevo_nodo = Nodo(data)
        if not self.head:
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo_nodo

    def buscar(self, criterio):
        actual = self.head
        while actual:
            if criterio(actual.data):
                return actual.data
            actual = actual.next
        return None

    def listar(self):
        elementos = []
        actual = self.head
        while actual:
            elementos.append(actual.data)
            actual = actual.next
        return elementos


class Tarea:
    def __init__(self, nombre, descripcion, estado="pendiente"):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado

    def __str__(self):
        return f"Tarea: {self.nombre}, Descripción: {self.descripcion}, Estado: {self.estado}"


class Proyecto:
    def __init__(self, id_proyecto, nombre):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.tareas = ListaEnlazada()

    def __str__(self):
        tareas = self.tareas.listar()
        tareas_str = "\n".join([str(tarea) for tarea in tareas])
        return f"Proyecto: {self.nombre} (ID: {self.id_proyecto})\nTareas:\n{tareas_str if tareas else 'No hay tareas'}"


class AdministradorProyectos:
    def __init__(self):
        self.proyectos = ListaEnlazada()

    def agregar_proyecto(self, id_proyecto, nombre):
        proyecto = Proyecto(id_proyecto, nombre)
        self.proyectos.agregar(proyecto)

    def agregar_tarea(self, id_proyecto, nombre_tarea, descripcion):
        proyecto = self.proyectos.buscar(lambda p: p.id_proyecto == id_proyecto)
        if proyecto:
            tarea = Tarea(nombre_tarea, descripcion)
            proyecto.tareas.agregar(tarea)
        else:
            print(f"Proyecto con ID {id_proyecto} no encontrado.")

    def cambiar_estado_tarea(self, id_proyecto, nombre_tarea, nuevo_estado):
        proyecto = self.proyectos.buscar(lambda p: p.id_proyecto == id_proyecto)
        if proyecto:
            tarea = proyecto.tareas.buscar(lambda t: t.nombre == nombre_tarea)
            if tarea:
                tarea.estado = nuevo_estado
            else:
                print(f"Tarea {nombre_tarea} no encontrada en el proyecto {id_proyecto}.")
        else:
            print(f"Proyecto con ID {id_proyecto} no encontrado.")

    def listar_proyectos(self):
        proyectos = self.proyectos.listar()
        for proyecto in proyectos:
            print(proyecto)


# Ejemplo de uso
if __name__ == "__main__":
    admin = AdministradorProyectos()

    # Agregar proyectos
    admin.agregar_proyecto(1, "Proyecto A")
    admin.agregar_proyecto(2, "Proyecto B")

    # Agregar tareas
    admin.agregar_tarea(1, "Tarea 1", "Descripción de la tarea 1")
    admin.agregar_tarea(1, "Tarea 2", "Descripción de la tarea 2")
    admin.agregar_tarea(2, "Tarea 3", "Descripción de la tarea 3")

    # Cambiar estado de una tarea
    admin.cambiar_estado_tarea(1, "Tarea 1", "en progreso")

    # Listar proyectos y tareas
    admin.listar_proyectos()
