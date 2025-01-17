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


class NodoTarea:
    def __init__(self, tarea):
        self.tarea = tarea
        self.siguiente = None
        self.anterior = None


class Proyecto:
    def __init__(self, id_proyecto, nombre):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.tareas = None
    
    def agregar_tarea_inicio(self, nombre_tarea, descripcion):
        nueva_tarea = NodoTarea(Tarea(nombre_tarea, descripcion))
        if self.tareas is None:
            self.tareas = nueva_tarea
        else:
            nueva_tarea.siguiente = self.tareas
            self.tareas.anterior = nueva_tarea
            self.tareas = nueva_tarea

    def agregar_tarea_final(self, nombre_tarea, descripcion):
        nueva_tarea = NodoTarea(Tarea(nombre_tarea, descripcion))
        if self.tareas is None:
            self.tareas = nueva_tarea
        else:
            actual = self.tareas
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva_tarea
            nueva_tarea.anterior = actual

    def insertar_tarea_en_posicion(self, nombre_tarea, descripcion, posicion):
        nueva_tarea = NodoTarea(Tarea(nombre_tarea, descripcion))
        if self.tareas is None:
            self.tareas = nueva_tarea
        else:
            actual = self.tareas
            contador = 0
            while actual and contador < posicion:
                actual = actual.siguiente
                contador += 1
            if actual is None:
                self.agregar_tarea_final(nombre_tarea, descripcion)
            else:
                nueva_tarea.siguiente = actual
                nueva_tarea.anterior = actual.anterior
                if actual.anterior:
                    actual.anterior.siguiente = nueva_tarea
                actual.anterior = nueva_tarea

    def eliminar_tarea(self, nombre_tarea):
        if self.tareas is None:
            raise ValueError("No hay tareas en este proyecto.")
        
        actual = self.tareas
        while actual:
            if actual.tarea.nombre == nombre_tarea:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                if actual == self.tareas:
                    self.tareas = actual.siguiente
                print(f"Tarea '{nombre_tarea}' eliminada.")
                return
            actual = actual.siguiente
        raise ValueError(f"Tarea '{nombre_tarea}' no encontrada.")

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
            actual = actual.siguiente
        while actual:
            print(actual.tarea)
            actual = actual.anterior


def menu():
    lista_proyectos = []

    while True:
        print("\n=== Sistema de Administracion de Proyectos ===")
        print("1. Agregar un nuevo proyecto")
        print("2. Agregar tarea al inicio de un proyecto")
        print("3. Agregar tarea al final de un proyecto")
        print("4. Insertar tarea en una posicion")
        print("5. Eliminar tarea de un proyecto")
        print("6. Recorrer tareas de un proyecto")
        print("7. Recorrer tareas de un proyecto de forma inversa")
        print("8. Listar todos los proyectos y sus tareas")
        print("9. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            id_proyecto = input("Ingrese el ID del proyecto: ")
            nombre_proyecto = input("Ingrese el nombre del proyecto: ")
            lista_proyectos.append(Proyecto(id_proyecto, nombre_proyecto))
            print("Proyecto agregado con exito.")
        
        elif opcion == '2':
            id_proyecto = input("Ingrese el ID del proyecto: ")
            nombre_tarea = input("Ingrese el nombre de la tarea: ")
            descripcion = input("Ingrese la descripcion de la tarea: ")

            proyecto = next((p for p in lista_proyectos if p.id_proyecto == id_proyecto), None)
            if proyecto:
                proyecto.agregar_tarea_inicio(nombre_tarea, descripcion)
                print("Tarea agregada al inicio con exito.")
            else:
                print(f"No se encontro el proyecto con ID: {id_proyecto}")

        elif opcion == '3':
            id_proyecto = input("Ingrese el ID del proyecto: ")
            nombre_tarea = input("Ingrese el nombre de la tarea: ")
            descripcion = input("Ingrese la descripcion de la tarea: ")

            proyecto = next((p for p in lista_proyectos if p.id_proyecto == id_proyecto), None)
            if proyecto:
                proyecto.agregar_tarea_final(nombre_tarea, descripcion)
                print("Tarea agregada al final con exito.")
            else:
                print(f"No se encontro el proyecto con ID: {id_proyecto}")

        elif opcion == '4':
            id_proyecto = input("Ingrese el ID del proyecto: ")
            nombre_tarea = input("Ingrese el nombre de la tarea: ")
            descripcion = input("Ingrese la descripcion de la tarea: ")
            posicion = int(input("Ingrese la posicion donde insertar la tarea: "))

            proyecto = next((p for p in lista_proyectos if p.id_proyecto == id_proyecto), None)
            if proyecto:
                proyecto.insertar_tarea_en_posicion(nombre_tarea, descripcion, posicion)
                print("Tarea insertada con exito en la posicion especificada.")
            else:
                print(f"No se encontro el proyecto con ID: {id_proyecto}")

        elif opcion == '5':
            id_proyecto = input("Ingrese el ID del proyecto: ")
            nombre_tarea = input("Ingrese el nombre de la tarea a eliminar: ")

            proyecto = next((p for p in lista_proyectos if p.id_proyecto == id_proyecto), None)
            if proyecto:
                try:
                    proyecto.eliminar_tarea(nombre_tarea)
                except ValueError as e:
                    print(e)
            else:
                print(f"No se encontro el proyecto con ID: {id_proyecto}")

        elif opcion == '6':
            id_proyecto = input("Ingrese el ID del proyecto: ")

            proyecto = next((p for p in lista_proyectos if p.id_proyecto == id_proyecto), None)
            if proyecto:
                proyecto.recorrer_tareas()
            else:
                print(f"No se encontro el proyecto con ID: {id_proyecto}")

        elif opcion == '7':
            id_proyecto = input("Ingrese el ID del proyecto: ")

            proyecto = next((p for p in lista_proyectos if p.id_proyecto == id_proyecto), None)
            if proyecto:
                proyecto.recorrer_tareas_reversa()
            else:
                print(f"No se encontro el proyecto con ID: {id_proyecto}")

        elif opcion == '8':
            for proyecto in lista_proyectos:
                print(f"Proyecto: {proyecto.nombre} (ID: {proyecto.id_proyecto})")
                proyecto.recorrer_tareas()

        elif opcion == '9':
            print("¡Gracias por usar el sistema!")
            break

        else:
            print("Opcion no valida. Intentelo nuevamente.")


menu()
