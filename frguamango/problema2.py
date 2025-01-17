class TareaCircular:
    def __init__(self, nombre, descripcion, estado="Pendiente"):
        # Inicializa una tarea con nombre, descripción y estado predeterminado "Pendiente"
        self.nombre = nombre  # Nombre de la tarea
        self.descripcion = descripcion  # Descripción de la tarea
        self.estado = estado  # Estado de la tarea (Pendiente, En progreso, Completada)
        self.siguiente = None  # Referencia al siguiente nodo (tarea)

class ListaCircularTareas:
    def __init__(self):
        # Inicializa una lista circular vacía para tareas
        self.cabeza = None  # Referencia a la primera tarea

    def agregar_tarea(self, nombre, descripcion):
        # Agrega una nueva tarea al final de la lista circular
        nueva_tarea = TareaCircular(nombre, descripcion)  # Crear nueva tarea
        if not self.cabeza:  # Si la lista está vacía
            self.cabeza = nueva_tarea  # La nueva tarea se convierte en la cabeza
            nueva_tarea.siguiente = nueva_tarea  # La cabeza apunta a sí misma
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:  # Recorre hasta el último nodo
                actual = actual.siguiente
            actual.siguiente = nueva_tarea  # El último nodo apunta a la nueva tarea
            nueva_tarea.siguiente = self.cabeza  # La nueva tarea apunta a la cabeza

    def eliminar_tarea(self, nombre_tarea):
        # Elimina una tarea específica por su nombre
        if not self.cabeza:  # Si la lista está vacía
            return False

        actual = self.cabeza
        anterior = None

        while True:
            if actual.nombre == nombre_tarea:  # Si encuentra la tarea por su nombre
                if anterior is None:  # Caso especial: eliminar la cabeza
                    if actual.siguiente == self.cabeza:  # Solo hay una tarea en la lista
                        self.cabeza = None  # La lista queda vacía
                    else:
                        temp = self.cabeza
                        while temp.siguiente != self.cabeza:  # Encuentra el último nodo
                            temp = temp.siguiente
                        temp.siguiente = actual.siguiente  # Actualiza la referencia del último nodo
                        self.cabeza = actual.siguiente  # Actualiza la cabeza
                else:
                    anterior.siguiente = actual.siguiente  # Salta el nodo actual
                return True
            anterior = actual
            actual = actual.siguiente
            if actual == self.cabeza:  # Si da la vuelta completa y no encuentra la tarea
                break
        return False

    def recorrer_circular(self, ciclos=1):
        # Recorre la lista circular un número de ciclos especificado
        if not self.cabeza:  # Si la lista está vacía
            return []

        actual = self.cabeza
        tareas = []  # Lista para almacenar las tareas en orden de recorrido
        for _ in range(ciclos):  # Repite el recorrido el número de ciclos indicado
            while True:
                tareas.append(f"{actual.nombre} - {actual.descripcion} - {actual.estado}")
                actual = actual.siguiente
                if actual == self.cabeza:  # Si vuelve a la cabeza, termina el ciclo
                    break
        return tareas

class ProyectoCircular:
    def __init__(self, id, nombre):
        # Inicializa un proyecto con ID único, nombre y una lista circular de tareas
        self.id = id  # ID único del proyecto
        self.nombre = nombre  # Nombre del proyecto
        self.tareas = ListaCircularTareas()  # Lista circular de tareas asociadas al proyecto

class ListaProyectosCirculares:
    def __init__(self):
        # Inicializa una lista enlazada vacía para proyectos
        self.cabeza = None

    def agregar_proyecto(self, id, nombre):
        # Agrega un nuevo proyecto al final de la lista enlazada
        nuevo_proyecto = ProyectoCircular(id, nombre)  # Crear nuevo proyecto
        if not self.cabeza:  # Si la lista está vacía
            self.cabeza = nuevo_proyecto  # El nuevo proyecto se convierte en la cabeza
        else:
            actual = self.cabeza
            while actual.siguiente:  # Recorre hasta el último nodo
                actual = actual.siguiente
            actual.siguiente = nuevo_proyecto  # Agrega el nuevo proyecto al final

    def obtener_proyecto(self, id):
        # Busca un proyecto por su ID en la lista enlazada
        actual = self.cabeza  # Inicia desde la cabeza
        while actual:  # Recorre la lista
            if actual.id == id:  # Si encuentra el proyecto por su ID
                return actual  # Retorna el proyecto
            actual = actual.siguiente
        return None  # Retorna None si no encuentra el proyecto

# Programa principal
def main():
    lista_proyectos = ListaProyectosCirculares()  # Inicializa la lista enlazada de proyectos

    while True:
        print("\n--- Menú ---")
        print("1. Agregar proyecto")
        print("2. Agregar tarea a proyecto")
        print("3. Eliminar tarea de un proyecto")
        print("4. Recorrer tareas de un proyecto")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            # Opción para agregar un nuevo proyecto
            id = input("ID del proyecto: ")
            nombre = input("Nombre del proyecto: ")
            lista_proyectos.agregar_proyecto(id, nombre)

        elif opcion == "2":
            # Opción para agregar una tarea a un proyecto existente
            id = input("ID del proyecto: ")
            proyecto = lista_proyectos.obtener_proyecto(id)  # Busca el proyecto por ID
            if proyecto:
                nombre_tarea = input("Nombre de la tarea: ")
                descripcion = input("Descripción de la tarea: ")
                proyecto.tareas.agregar_tarea(nombre_tarea, descripcion)  # Agrega la tarea al proyecto
            else:
                print("Proyecto no encontrado.")

        elif opcion == "3":
            # Opción para eliminar una tarea de un proyecto específico
            id = input("ID del proyecto: ")
            proyecto = lista_proyectos.obtener_proyecto(id)  # Busca el proyecto por ID
            if proyecto:
                nombre_tarea = input("Nombre de la tarea a eliminar: ")
                if not proyecto.tareas.eliminar_tarea(nombre_tarea):
                    print("Tarea no encontrada.")
                else:
                    print("Tarea eliminada correctamente.")
            else:
                print("Proyecto no encontrado.")

        elif opcion == "4":
            # Opción para recorrer las tareas de un proyecto de forma cíclica
            id = input("ID del proyecto: ")
            proyecto = lista_proyectos.obtener_proyecto(id)  # Busca el proyecto por ID
            if proyecto:
                ciclos = int(input("¿Cuántos ciclos deseas recorrer? "))
                tareas = proyecto.tareas.recorrer_circular(ciclos)  # Recorre las tareas
                for tarea in tareas:
                    print(tarea)  # Imprime cada tarea en el orden del recorrido
            else:
                print("Proyecto no encontrado.")

        elif opcion == "5":
            # Salir del programa
            break

        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
