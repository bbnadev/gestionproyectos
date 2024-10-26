from controllers.proyecto_controller import ProyectoController, Proyecto
from datetime import datetime


class ProyectoView:
    def __init__(self):
        self.controller = ProyectoController()

    def crear(self):
        nombre = input("Ingrese el nombre del Proyecto: ")
        if not nombre:
            print("El nombre es requerido.")
            return

        if self.controller.buscar_por_nombre(nombre):
            print("Ya existe un proyecto con ese nombre.")
            return

        desc = input("Ingrese descripción del Proyecto: ")

        fecha_inicio = input(
            "Ingrese fecha de inicio del Proyecto (YYYY-MM-DD): ")
        fecha_inicio = fecha_inicio if fecha_inicio else datetime.now()

        nuevo_proyecto = Proyecto(
            nombre=nombre,
            descripcion=desc,
            fecha_inicio=fecha_inicio
        )
        id = self.controller.crear(nuevo_proyecto)
        print(f"El proyecto se creo exitosamente con ID: {id}")

    def listar(self):
        proyectos = self.controller.listar()
        if not proyectos:
            print("No hay proyectos registrados.")
            return

        for proyecto in proyectos:
            print(proyecto)

    def buscar_por_id(self):
        id_proyecto = int(input("Ingrese el ID del proyecto a buscar: "))

        if not id_proyecto:
            print("El ID es requerido.")
            return

        proyecto = self.controller.buscar_por_id(id_proyecto)
        if not proyecto:
            print("Proyecto no encontrado.")
            return
        print(proyecto)

    def buscar_por_nombre(self):
        nombre = input("Ingrese el nombre del proyecto a buscar: ")

        if not nombre:
            print("El nombre es requerido.")
            return

        proyecto = self.controller.buscar_por_nombre(nombre)
        if not proyecto:
            print("Proyecto no encontrado.")
            return
        print(proyecto)

    def modificar(self):
        id_proyecto = input("Ingrese el ID del proyecto a modificar: ")
        if not id_proyecto:
            print("El ID es requerido.")
            return

        proyecto = self.controller.buscar_por_id(id_proyecto)

        if not proyecto:
            print("Proyecto no encontrado.")
            return

        proyecto = Proyecto(*proyecto)
        nombre = input("Ingrese el nuevo nombre del Proyecto: ")
        if not nombre:
            nombre = proyecto.get_nombre()

        desc = input("Ingrese nueva descripción del Proyecto: ")
        if not desc:
            desc = proyecto.get_descripcion()

        fecha_inicio = input(
            "Ingrese nueva fecha de inicio del Proyecto (YYYY-MM-DD): ")
        if not fecha_inicio:
            fecha_inicio = proyecto.get_fecha_inicio()

        proyecto_modificado = Proyecto(
            id=id_proyecto,
            nombre=nombre,
            descripcion=desc,
            fecha_inicio=fecha_inicio
        )
        self.controller.modificar(proyecto_modificado)
        print(f"El proyecto \"{nombre}\" se modificó exitosamente.")

    def eliminar(self):
        id_proyecto = input("Ingrese el ID del proyecto a eliminar: ")
        if not id_proyecto:
            print("El ID es requerido.")
            return

        proyecto = self.controller.buscar_por_id(id_proyecto)
        if not proyecto:
            print("Proyecto no encontrado.")
            return

        self.controller.eliminar(id_proyecto)
        print(f"El proyecto \"{proyecto[1]}\" se eliminó exitosamente.")

    def agregar_empleado(self):
        id_proyecto = input("Ingrese el ID del proyecto: ")
        if not id_proyecto:
            print("El ID es requerido.")
            return

        proyecto = self.controller.buscar_por_id(id_proyecto)

        if not proyecto:
            print("Proyecto no encontrado.")
            return

        rut_empleado = input("Ingrese el RUT del empleado: ")
        if not rut_empleado:
            print("El RUT es requerido.")
            return

        if len(rut_empleado.split("-")) != 2:
            print("El RUT debe tener un guión.")
            return

        if len(rut_empleado.split("-")[0]) == 0:
            print("El RUT debe tener dígitos antes del verificador.")
            return

        if len(rut_empleado.split("-")[1]) != 1:
            print("El RUT debe tener un dígito verificador.")
            return

        from controllers.empleado_controller import EmpleadoController, Empleado
        empleado_controller = EmpleadoController()
        empleado = empleado_controller.buscar_por_rut(rut_empleado)
        if not empleado:
            print("Empleado no encontrado.")
            return

        empleado = Empleado(*empleado)
        self.controller.agregar_empleado(id_proyecto, empleado.get_id())
        print(f"Empleado {empleado.get_nombre()} agregado exitosamente al proyecto {
              proyecto[1]}.")

    def quitar_empleado(self):
        id_proyecto = input("Ingrese el ID del proyecto: ")
        if not id_proyecto:
            print("El ID es requerido.")
            return

        proyecto = self.controller.buscar_por_id(id_proyecto)
        if not proyecto:
            print("Proyecto no encontrado.")
            return

        rut_empleado = input("Ingrese el RUT del empleado: ")

        if not rut_empleado:
            print("El RUT es requerido.")
            return

        if len(rut_empleado.split("-")) != 2:
            print("El RUT debe tener un guión.")
            return

        if len(rut_empleado.split("-")[0]) == 0:
            print("El RUT debe tener dígitos antes del verificador.")
            return

        if len(rut_empleado.split("-")[1]) != 1:
            print("El RUT debe tener un dígito verificador.")
            return

        from controllers.empleado_controller import EmpleadoController, Empleado
        empleado_controller = EmpleadoController()
        empleado = empleado_controller.buscar_por_rut(rut_empleado)
        if not empleado:
            print("Empleado no encontrado.")
            return

        empleado = Empleado(*empleado)
        self.controller.quitar_empleado(id_proyecto, empleado.get_id())
        print(f"Empleado {empleado.get_nombre()} quitado exitosamente del proyecto {
              proyecto[1]}.")

    def listar_empleados(self):
        id_proyecto = input("Ingrese el ID del proyecto: ")

        if not id_proyecto:
            print("El ID es requerido.")
            return

        proyecto = self.controller.buscar_por_id(id_proyecto)
        if not proyecto:
            print("Proyecto no encontrado.")
            return

        empleados = self.controller.listar_empleados(id_proyecto)
        if not empleados:
            print("No hay empleados en este proyecto.")
            return

        print(f"Empleados del proyecto {proyecto[1]}:")
        for empleado in empleados:
            print(empleado)
