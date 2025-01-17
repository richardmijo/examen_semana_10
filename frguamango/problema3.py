class TareaDoble:
    def __init__(self, nombre, descripcion, estado="Pendiente"):
        # Inicializa una tarea con nombre, descripción y estado predeterminado "Pendiente"
        self.nombre = nombre  # Nombre de la tarea
        self.descripcion = descripcion  # Descripción de la tarea
        self.estado = estado  # Estado de la tarea (Pendiente, En progreso, Completada)
        self.anterior = None  # Referencia al nodo anterior
        self.siguiente = None  # Referencia al nodo siguiente

class ListaDobleTareas:
    def __init__(self):
        # Inicializa una lista doblemente enlazada vacía para tareas
        self.cabeza = None  # Referencia a la primera tarea
        self.cola = None  # Referencia a la última tarea

    def agregar_tarea(self, nombre, descripcion):
        # Agrega una nueva tarea al final de la lista doblemente enlazada
        nueva_tarea = TareaDoble(nombre, descripcion)  # Crear nueva tarea
        if not self.cabeza:  # Si la lista está vacía
            self.cabeza = nueva_tarea  # La nueva tarea se convierte en la cabeza
            self.cola = nueva_tarea  # También se convierte en la cola
        else:
            nueva_tarea.anterior = self.cola  # La nueva tarea apunta al nodo actual de la cola
            self.cola.siguiente = nueva_tarea  # La cola actual apunta a la nueva tarea
            self.cola = nueva_tarea  # Actualiza la cola a la nueva tarea

    def insertar_tarea(self, posicion, nombre, descripcion):
        # Inserta una tarea en una posición específica
        nueva_tarea = TareaDoble(nombre, descripcion)  # Crear nueva tarea
        if posicion == 0:  # Insertar al inicio
            if not self.cabeza:  # Si la lista está vacía
                self.cabeza = nueva_tarea
                self.cola = nueva_tarea
            else:
                nueva_tarea.siguiente = self.cabeza  # La nueva tarea apunta a la cabeza actual
                self.cabeza.anterior = nueva_tarea  # La cabeza actual apunta a la nueva tarea
                self.cabeza = nueva_tarea  # La nueva tarea se convierte en la cabeza
        else:
            actual = self.cabeza
            indice = 0
            while actual and indice < posicion:
                anterior = actual
                actual = actual.siguiente
                indice += 1
            if actual:  # Insertar en medio
                nueva_tarea.siguiente = actual
                nueva_tarea.anterior = actual.anterior
                if actual.anterior:
                    actual.anterior.siguiente = nueva_tarea
                actual.anterior = nueva_tarea
            else:  # Insertar al final
                self.agregar_tarea(nombre, descripcion)

    def eliminar_tarea(self, nombre):
        # Elimina una tarea específica por su nombre
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre:  # Si encuentra la tarea por su nombre
                if actual.anterior:  # Si no es la cabeza
                    actual.anterior.siguiente = actual.siguiente
                else:  # Si es la cabeza
                    self.cabeza = actual.siguiente
                if actual.siguiente:  # Si no es la cola
                    actual.siguiente.anterior = actual.anterior
                else:  # Si es la cola
                    self.cola = actual.anterior
                return True  # Retorna True si la tarea fue eliminada
            actual = actual.siguiente
        return False  # Retorna False si la tarea no fue encontrada

    def listar_tareas(self):
        # Lista todas las tareas con sus detalles
        actual = self.cabeza
        tareas = []
        while actual:  # Recorre la lista de la cabeza a la cola
            tareas.append(f"{actual.nombre} - {actual.descripcion} - {actual.estado}")
            actual = actual.siguiente
        return tareas

class ProyectoDoble:
    def __init__(self, id, nombre):
        # Inicializa un proyecto con ID único, nombre y una lista doblemente enlazada de tareas
        self.id = id  # ID único del proyecto
        self.nombre = nombre  # Nombre del proyecto
        self.tareas = ListaDobleTareas()  # Lista doblemente enlazada de tareas asociadas al proyecto

class ListaProyectosDobles:
    def __init__(self):
        # Inicializa una lista enlazada vacía para proyectos
        self.cabeza = None

    def agregar_proyecto(self, id, nombre):
        # Agrega un nuevo proyecto al final de la lista enlazada
        nuevo_proyecto = ProyectoDoble(id, nombre)  # Crear nuevo proyecto
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
    lista_proyectos = ListaProyectosDobles()  # Inicializa la lista enlazada de proyectos

    while True:
        print("\n--- Menú ---")
        print("1. Agregar proyecto")
        print("2. Agregar tarea a proyecto")
        print("3. Insertar tarea en posición específica")
        print("4. Eliminar tarea de un proyecto")
        print("5. Listar proyectos y tareas")
        print("6. Salir")

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
            # Opción para insertar una tarea en una posición específica
            id = input("ID del proyecto: ")
            proyecto = lista_proyectos.obtener_proyecto(id)  # Busca el proyecto por ID
            if proyecto:
                posicion = int(input("Posición para insertar la tarea: "))
                nombre_tarea = input("Nombre de la tarea: ")
                descripcion = input("Descripción de la tarea: ")
                proyecto.tareas.insertar_tarea(posicion, nombre_tarea, descripcion)  # Inserta la tarea
            else:
                print("Proyecto no encontrado.")

        elif opcion == "4":
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

        elif opcion == "5":
            # Opción para listar todos los proyectos y sus tareas
            actual = lista_proyectos.cabeza
            while actual:
                print(f"Proyecto {actual.id} - {actual.nombre}")
                tareas = actual.tareas.listar_tareas()  # Lista las tareas del proyecto
                for tarea in tareas:
                    print(f"  {tarea}")  # Imprime las tareas con indentación
                actual = actual.siguiente

        elif opcion == "6":
            # Salir del programa
            break

        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
