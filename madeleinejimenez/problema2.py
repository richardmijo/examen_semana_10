class Nodo:
    def __init__(self, data):
        self.data = data  # Contiene el objeto (proyecto o tarea)
        self.next = None  # Referencia al siguiente nodo


class ListaCircular:
    def __init__(self):
        self.head = None  # Nodo inicial de la lista

    def agregar(self, data):
        nuevo_nodo = Nodo(data)
        if not self.head:
            self.head = nuevo_nodo
            nuevo_nodo.next = self.head  # Apunta a sí mismo
        else:
            actual = self.head
            while actual.next != self.head:
                actual = actual.next
            actual.next = nuevo_nodo
            nuevo_nodo.next = self.head

    def eliminar(self, criterio):
        if not self.head:
            return False

        actual = self.head
        anterior = None

        while True:
            if criterio(actual.data):
                if anterior is None:  # Eliminar el nodo head
                    if actual.next == self.head:  # Solo un nodo en la lista
                        self.head = None
                    else:
                        temp = self.head
                        while temp.next != self.head:
                            temp = temp.next
                        temp.next = self.head.next
                        self.head = self.head.next
                else:  # Eliminar un nodo intermedio o final
                    anterior.next = actual.next
                return True

            anterior = actual
            actual = actual.next

            if actual == self.head:
                break

        return False

    def recorrer_circular(self, n):
        if not self.head:
            return

        actual = self.head
        contador = 0
        while contador < n:  # Para evitar un bucle infinito
            yield actual.data
            actual = actual.next
            contador += 1


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
        self.tareas = ListaCircular()

    def __str__(self):
        tareas = list(self.tareas.recorrer_circular(10))  # Muestra hasta 10 tareas para evitar bucles infinitos
        tareas_str = "\n".join([str(tarea) for tarea in tareas])
        return f"Proyecto: {self.nombre} (ID: {self.id_proyecto})\nTareas:\n{tareas_str if tareas else 'No hay tareas'}"


class AdministradorProyectos:
    def __init__(self):
        self.proyectos = ListaCircular()

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

    def eliminar_tarea(self, id_proyecto, nombre_tarea):
        proyecto = self.proyectos.buscar(lambda p: p.id_proyecto == id_proyecto)
        if proyecto:
            eliminado = proyecto.tareas.eliminar(lambda t: t.nombre == nombre_tarea)
            if eliminado:
                print(f"Tarea {nombre_tarea} eliminada del proyecto {id_proyecto}.")
            else:
                print(f"Tarea {nombre_tarea} no encontrada en el proyecto {id_proyecto}.")
        else:
            print(f"Proyecto con ID {id_proyecto} no encontrado.")

    def recorrer_tareas(self, id_proyecto, n):
        proyecto = self.proyectos.buscar(lambda p: p.id_proyecto == id_proyecto)
        if proyecto:
            for tarea in proyecto.tareas.recorrer_circular(n):
                print(tarea)
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
    admin.agregar_tarea(1, "Tarea 3", "Descripción de la tarea 3")

    # Recorrer tareas de forma circular
    print("Recorriendo tareas del Proyecto A:")
    admin.recorrer_tareas(1, 5)

    # Eliminar tarea
    admin.eliminar_tarea(1, "Tarea 2")

    # Listar proyectos y tareas
    print("\nProyectos actualizados:")
    admin.listar_proyectos()
