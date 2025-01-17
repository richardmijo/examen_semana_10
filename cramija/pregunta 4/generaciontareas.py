class Tarea:
    def __init__(self, nombre, descripcion, estado="pendiente"):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado
        self.siguiente = None
        self.anterior = None  

class Proyecto:
    def __init__(self, id_proyecto, nombre):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.tareas = None

    def agregar_tarea(self, nombre_tarea, descripcion):
        nueva_tarea = Tarea(nombre_tarea, descripcion)
        if not self.tareas:
            self.tareas = nueva_tarea
        else:
            actual = self.tareas
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva_tarea
            nueva_tarea.anterior = actual

    def listar_tareas(self, tarea=None):
        
        if tarea is None:
            tarea = self.tareas
        
        
        if tarea is None:
            return
        
        
        print(f"Tarea: {tarea.nombre}, Descripción: {tarea.descripcion}, Estado: {tarea.estado}")
        
        
        self.listar_tareas(tarea.siguiente)

    def generar_tareas_recursivo(self, id_inicio, id_fin, descripcion_base, tarea=None):
        if id_inicio > id_fin:
            return
        
        nombre_tarea = f"Tarea {id_inicio}"
        descripcion = f"{descripcion_base} {id_inicio}"
        
        
        self.agregar_tarea(nombre_tarea, descripcion)
        
        
        self.generar_tareas_recursivo(id_inicio + 1, id_fin, descripcion_base)


def interactuar_con_usuario():
    # PROTECTO
    proyecto = Proyecto(1, "Proyecto de Grado")

    
    print("Generación automática de tareas:")
    id_inicio = int(input("Ingrese el ID inicial de las tareas: "))
    id_fin = int(input("Ingrese el ID final de las tareas: "))
    descripcion_base = input("Ingrese la descripción base de las tareas: ")

    # GENERAR TAREAS AUTOMATICAS
    proyecto.generar_tareas_recursivo(id_inicio, id_fin, descripcion_base)

    # TAREAS GENERADAS
    print("\nLista de tareas generadas:")
    proyecto.listar_tareas()


interactuar_con_usuario()