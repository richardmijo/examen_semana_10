class NodoDoble:
    def __init__(self, data):
        self.data = data  # Contiene el objeto (proyecto o tarea)
        self.next = None  # Referencia al siguiente nodo
        self.prev = None  # Referencia al nodo anterior


class ListaDoblementeEnlazada:
    def __init__(self):
        self.head = None  # Nodo inicial de la lista
        self.tail = None  # Nodo final de la lista

    def agregar_final(self, data):
        nuevo_nodo = NodoDoble(data)
        if not self.head:
            self.head = self.tail = nuevo_nodo
        else:
            self.tail.next = nuevo_nodo
            nuevo_nodo.prev = self.tail
            self.tail = nuevo_nodo

    def insertar_en_posicion(self, data, posicion):
        nuevo_nodo = NodoDoble(data)
        if posicion == 0:  # Insertar al inicio
            if not self.head:
                self.head = self.tail = nuevo_nodo
            else:
                nuevo_nodo.next = self.head
                self.head.prev = nuevo_nodo
                self.head = nuevo_nodo
        else:
            actual = self.head
            indice = 0
            while actual and indice < posicion - 1:
                actual = actual.next
                indice += 1
            if actual:  # Insertar en el medio o al final
                nuevo_nodo.next = actual.next
                nuevo_nodo.prev = actual
                if actual.next:
                    actual.next.prev = nuevo_nodo
                actual.next = nuevo_nodo
                if nuevo_nodo.next is None:  # Actualizar la cola si es necesario
                    self.tail = nuevo_nodo

    def eliminar_por_criterio(self, criterio):
        actual = self.head
        while actual:
            if criterio(actual.data):
                if actual.prev:
                    actual.prev.next = actual.next
                if actual.next:
                    actual.next.prev = actual.prev
                if actual == self.head:  # Si es el nodo inicial
                    self.head = actual.next
                if actual == self.tail:  # Si es el nodo final
                    self.tail = actual.prev
                return True
            actual = actual.next
        return False

    def listar(self):
        elementos = []
        actual = self.head
        while actual:
            elementos.append(actual.data)
            actual = actual.next
        return elementos

    def listar_inverso(self):
        elementos = []
        actual = self.tail
        while actual:
            elementos.append(actual.data)
            actual = actual.prev
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
        self.tareas = ListaDoblementeEnlazada()

    def __str__(self):
        tareas = self.tareas.listar()
        tareas_str = "\n".join([str(tarea) for tarea in tareas])
        return f"Proyecto: {self.nombre} (ID: {self.id_proyecto})\nTareas:\n{tareas_str if tareas else 'No hay tareas'}"


class AdministradorProyectos:
    def __init__(self):
        self.proyectos = ListaDoblementeEnlazada()

    def agregar_proyecto(self, id_proyecto, nombre):
        proyecto = Proyecto(id_proyecto, nombre)
        self.proyectos.agregar_final(proyecto)

    def agregar_tarea(self, id_proyecto, nombre_tarea, descripcion):
        proyecto = self.proyectos.listar()
        proyecto = next((p for p in proyecto if p.id_proyecto == id_proyecto), None)
        if proyecto:
            tarea = Tarea(nombre_tarea, descripcion)
            proyecto.tareas.agregar_final(tarea)
        else:
            print(f"Proyecto con ID {id_proyecto} no encontrado.")

    def insertar_tarea(self, id_proyecto, nombre_tarea, descripcion, posicion):
        proyecto = self.proyectos.listar()
        proyecto = next((p for p in proyecto if p.id_proyecto == id_proyecto), None)
        if proyecto:
            tarea = Tarea(nombre_tarea, descripcion)
            proyecto.tareas.insertar_en_posicion(tarea, posicion)
        else:
            print(f"Proyecto con ID {id_proyecto} no encontrado.")

    def eliminar_tarea(self, id_proyecto, nombre_tarea):
        proyecto = self.proyectos.listar()
        proyecto = next((p for p in proyecto if p.id_proyecto == id_proyecto), None)
        if proyecto:
            eliminado = proyecto.tareas.eliminar_por_criterio(lambda t: t.nombre == nombre_tarea)
            if eliminado:
                print(f"Tarea {nombre_tarea} eliminada del proyecto {id_proyecto}.")
            else:
                print(f"Tarea {nombre_tarea} no encontrada en el proyecto {id_proyecto}.")
        else:
            print(f"Proyecto con ID {id_proyecto} no encontrado.")

    def listar_proyectos(self):
        proyectos = self.proyectos.listar()
        for proyecto in proyectos:
            print(proyecto)

    def generar_tareas_recursivo(self, proyecto, id_inicial, id_final, descripcion_base):
        if id_inicial > id_final:
            return

        nombre_tarea = f"Tarea {id_inicial}"
        tarea = Tarea(nombre_tarea, f"{descripcion_base} {id_inicial}")
        proyecto.tareas.agregar_final(tarea)

        self.generar_tareas_recursivo(proyecto, id_inicial + 1, id_final, descripcion_base)


# Ejemplo de uso
if __name__ == "__main__":
    admin = AdministradorProyectos()

    # Agregar proyectos
    admin.agregar_proyecto(1, "Proyecto A")

    # Obtener proyecto
    proyecto = admin.proyectos.listar()[0]

    # Generar tareas recursivamente
    admin.generar_tareas_recursivo(proyecto, 1, 5, "Descripción base para tarea")

    # Listar proyectos y sus tareas
    admin.listar_proyectos()
