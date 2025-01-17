# Tarea representa una tarea dentro de un proyecto
class Tarea:
    def __init__(self, nombre, descripcion, estado='pendiente'):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in ['pendiente', 'en progreso', 'completada']:
            self.estado = nuevo_estado
        else:
            raise ValueError("Estado invalido. Use: 'pendiente', 'en progreso' o 'completada'.")

    def __str__(self):
        return f"Tarea: {self.nombre} | Estado: {self.estado} | Descripcion: {self.descripcion}"


# NodoTarea representara cada tarea dentro de la lista doblemente enlazada
class NodoTarea:
    def __init__(self, tarea):
        self.tarea = tarea
        self.siguiente = None
        self.anterior = None


# Proyecto ahora tiene una lista doblemente enlazada de tareas
class Proyecto:
    def __init__(self, id_proyecto, nombre):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.tareas = None  # Lista doblemente enlazada de tareas.
    
    def agregar_tarea_final(self, nombre_tarea, descripcion):
        nueva_tarea = NodoTarea(Tarea(nombre_tarea, descripcion))
        if self.tareas is None:
            self.tareas = nueva_tarea
        else:
            actual = self.tareas
            while actual.siguiente:  # Recorre hasta el final
                actual = actual.siguiente
            actual.siguiente = nueva_tarea
            nueva_tarea.anterior = actual

    def recorrer_tareas(self):
        if self.tareas is None:
            print("No hay tareas en este proyecto.")
            return
        actual = self.tareas
        while actual:
            print(actual.tarea)
            actual = actual.siguiente
    
    def recorrer_tareas_reversa(self):
        if self.tareas is None:
            print("No hay tareas en este proyecto.")
            return
        actual = self.tareas
        while actual.siguiente:
            actual = actual.siguiente  # Llegar al ultimo nodo
        while actual:
            print(actual.tarea)
            actual = actual.anterior

    def generar_tareas_recursivo(self, id_inicial, id_final, descripcion_base):
        """Genera tareas recursivamente desde id_inicial hasta id_final"""
        if id_inicial > id_final:
            return  # Caso base: si el ID inicial es mayor al final, se termina la recursion.
        # Crear tarea
        nombre_tarea = f"Tarea {id_inicial}"
        descripcion = f"{descripcion_base} {id_inicial}"
        self.agregar_tarea_final(nombre_tarea, descripcion)
        # Llamada recursiva
        self.generar_tareas_recursivo(id_inicial + 1, id_final, descripcion_base)


# Funcion para interactuar con el sistema
def menu():
    lista_proyectos = []

    while True:
        print("\n=== Sistema de Administracion de Proyectos ===")
        print("1. Agregar un nuevo proyecto")
        print("2. Generar tareas automaticamente (recursivo)")
        print("3. Recorrer tareas de un proyecto")
        print("4. Recorrer tareas de un proyecto de forma inversa")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            id_proyecto = input("Ingrese el ID del proyecto: ")
            nombre_proyecto = input("Ingrese el nombre del proyecto: ")
            lista_proyectos.append(Proyecto(id_proyecto, nombre_proyecto))
            print("Proyecto agregado con exito.")
        
        elif opcion == '2':
            id_proyecto = input("Ingrese el ID del proyecto: ")
            id_inicial = int(input("Ingrese el ID inicial de las tareas: "))
            id_final = int(input("Ingrese el ID final de las tareas: "))
            descripcion_base = input("Ingrese la descripcion base de las tareas: ")

            proyecto = next((p for p in lista_proyectos if p.id_proyecto == id_proyecto), None)
            if proyecto:
                proyecto.generar_tareas_recursivo(id_inicial, id_final, descripcion_base)
                print(f"Tareas generadas automaticamente para el proyecto '{proyecto.nombre}'.")
            else:
                print(f"No se encontro el proyecto con ID: {id_proyecto}")

        elif opcion == '3':
            id_proyecto = input("Ingrese el ID del proyecto: ")

            proyecto = next((p for p in lista_proyectos if p.id_proyecto == id_proyecto), None)
            if proyecto:
                proyecto.recorrer_tareas()
            else:
                print(f"No se encontro el proyecto con ID: {id_proyecto}")

        elif opcion == '4':
            id_proyecto = input("Ingrese el ID del proyecto: ")

            proyecto = next((p for p in lista_proyectos if p.id_proyecto == id_proyecto), None)
            if proyecto:
                proyecto.recorrer_tareas_reversa()
            else:
                print(f"No se encontro el proyecto con ID: {id_proyecto}")

        elif opcion == '5':
            print("¡Gracias por usar el sistema!")
            break

        else:
            print("Opcion no valida. Intentelo nuevamente.")


# Ejecutar el menu
menu()
