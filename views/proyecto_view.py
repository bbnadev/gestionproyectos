from controllers.proyecto_controller import ProyectoController
from models.proyecto import Proyecto


class ProyectoView:
    def __init__(self):
        self.controller = ProyectoController()

    def crear(self):
        nombre = input("Ingrese el nombre del Proyecto: ")
        desc = input("Ingrese descripción del Proyecto: ")
        fecha_inicio = input(
            "Ingrese fecha de inicio del Proyecto (YYYY-MM-DD): ")
        nuevo_proyecto = Proyecto(
            nombre=nombre,
            descripcion=desc,
            fecha_inicio=fecha_inicio
        )
        id = self.controller.crear(nuevo_proyecto)
        print(f"El proyecto \"{nombre}\" se creo exitosamente con ID: {id}")

    def listar(self):
        proyectos = self.controller.listar()
        for proyecto in proyectos:
            print(f"ID: {proyecto[0]}, Nombre: {proyecto[1]}, Descripción: {
                  proyecto[2]}, Fecha de inicio: {proyecto[3]}")

    def buscar_por_id(self):
        id_proyecto = int(input("Ingrese el ID del proyecto a buscar: "))
        proyecto = self.controller.buscar_por_id(id_proyecto)
        if proyecto:
            proyecto = Proyecto(*proyecto)
            print(f"ID: {proyecto.get_id()}\nNombre: {proyecto.get_nombre()}\nDescripción: {
                  proyecto.get_descripcion()}\nFecha de inicio: {proyecto.get_fecha_inicio()}")
        else:
            print("Proyecto no encontrado.")

    def buscar_por_nombre(self):
        nombre = input("Ingrese el nombre del proyecto a buscar: ")
        proyecto = self.controller.buscar_por_nombre(nombre)
        if proyecto:
            proyecto = Proyecto(*proyecto)
            print(f"ID: {proyecto.get_id()}\nNombre: {proyecto.get_nombre()}\nDescripción: {
                  proyecto.get_descripcion()}\nFecha de inicio: {proyecto.get_fecha_inicio()}")
        else:
            print("Proyecto no encontrado.")

    def modificar(self):
        id_proyecto = int(input("Ingrese el ID del proyecto a modificar: "))
        proyecto = self.controller.buscar_por_id(id_proyecto)
        if proyecto:
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
        else:
            print("Proyecto no encontrado.")

    def eliminar(self):
        id_proyecto = int(input("Ingrese el ID del proyecto a eliminar: "))
        proyecto = self.controller.buscar_por_id(id_proyecto)
        if proyecto:
            self.controller.eliminar(id_proyecto)
            print(f"El proyecto \"{proyecto[1]}\" se eliminó exitosamente.")
        else:
            print("Proyecto no encontrado.")

    def agregar_empleado(self):
        id_proyecto = int(input("Ingrese el ID del proyecto: "))
        proyecto: Proyecto = self.controller.buscar_por_id(id_proyecto)
        if not proyecto:
            print("Proyecto no encontrado.")
            return

        rut_empleado = input("Ingrese el RUT del empleado: ")

        from controllers.empleado_controller import EmpleadoController, Empleado
        empleado_controller = EmpleadoController()
        empleado: Empleado = empleado_controller.buscar_por_rut(rut_empleado)
        if not empleado:
            print("Empleado no encontrado.")
            return

        self.controller.agregar_empleado(id_proyecto, empleado.get_id())
        print(f"Empleado {empleado.get_nombre()} agregado exitosamente al proyecto {
              proyecto.get_nombre()}.")

    def quitar_empleado(self):
        id_proyecto = int(input("Ingrese el ID del proyecto: "))
        proyecto: Proyecto = self.controller.buscar_por_id(id_proyecto)
        if not proyecto:
            print("Proyecto no encontrado.")
            return

        rut_empleado = input("Ingrese el RUT del empleado: ")

        from controllers.empleado_controller import EmpleadoController, Empleado
        empleado_controller = EmpleadoController()
        empleado: Empleado = empleado_controller.buscar_por_rut(rut_empleado)
        if not empleado:
            print("Empleado no encontrado.")
            return

        self.controller.quitar_empleado(id_proyecto, empleado.get_id())
        print(f"Empleado {empleado.get_nombre()} quitado exitosamente del proyecto {
              proyecto.get_nombre()}.")

    def listar_empleados(self):
        id_proyecto = int(input("Ingrese el ID del proyecto: "))
        proyecto: Proyecto = self.controller.buscar_por_id(id_proyecto)
        if not proyecto:
            print("Proyecto no encontrado.")
            return

        empleados = self.controller.listar_empleados(id_proyecto)
        if empleados:
            print(f"Empleados del proyecto {proyecto.get_nombre()}:")
            for empleado in empleados:
                print(f"RUT: {empleado[0]}, Nombre: {empleado[1]}, Dirección: {
                      empleado[2]}, Teléfono: {empleado[3]}, Email: {empleado[4]}, Fecha de inicio: {empleado[5]}, Salario: {empleado[6]}, ID Departamento: {empleado[7]}")
        else:
            print("No hay empleados en este proyecto.")
