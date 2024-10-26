from controllers.registro_tiempo_controller import RegistroTiempoController, RegistroTiempo
from controllers.proyecto_controller import ProyectoController, Proyecto
from controllers.empleado_controller import EmpleadoController, Empleado
from datetime import datetime


class RegistroTiempoView:
    def __init__(self):
        self.controller = RegistroTiempoController()

    def crear(self):
        proyectoController = ProyectoController()
        empleadoController = EmpleadoController()

        rut_empleado = input("Ingrese el RUT del empleado: ")

        if not rut_empleado:
            print("RUT no puede estar vacío")
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

        empleado = empleadoController.buscar_por_rut(rut_empleado)

        if not empleado:
            print("Empleado no encontrado")
            return

        id_proyecto = input("Ingrese el ID del Proyecto: ")
        if not id_proyecto:
            print("ID de Proyecto no puede estar vacío")
            return

        proyecto = proyectoController.buscar_por_id(id_proyecto)
        if not proyecto:
            print("Proyecto no encontrado")
            return

        fecha = input("Ingrese la fecha: ")
        fecha = fecha if fecha else datetime.now()

        horas_trabajadas = input("Ingrese las horas trabajadas: ")
        if not horas_trabajadas:
            print("Horas trabajadas no puede estar vacío")
            return

        descripcion = input("Ingrese la descripción: ")

        nuevo_registro = RegistroTiempo(
            fecha=fecha,
            horas_trabajadas=float(horas_trabajadas),
            descripcion=descripcion,
            id_empleado=empleado[0],
            id_proyecto=int(id_proyecto)
        )

        id = self.controller.crear(nuevo_registro)
        print("Registro de tiempo creado con éxito con el ID:", id)

    def listar(self):
        registros = self.controller.listar()
        if not registros:
            print("No hay registros de tiempo.")
            return
        for registro in registros:
            print(registro)

    def buscar_por_id(self):
        id = input("Ingrese el ID del registro de tiempo a buscar: ")
        if not id:
            print("ID no puede estar vacío.")
            return
        registro = self.controller.buscar_por_id(id)
        if not registro:
            print("Registro de tiempo no encontrado.")
            return
        print(registro)

    def modificar(self):

        id_registro = input("Ingrese ID del registro: ")
        if not id_registro:
            print("ID no puede estar vacío.")
            return

        registro = self.controller.buscar_por_id(id_registro)
        if not registro:
            print("Registro no encontrado.")
            return

        registro = RegistroTiempo(*registro)

        fecha = input("Ingrese fecha (YYYY-MM-DD): ")
        fecha = fecha if fecha else registro.get_fecha()

        horas_trabajadas = input("Ingrese horas trabajadas: ")
        horas_trabajadas = horas_trabajadas if horas_trabajadas else registro.get_horas_trabajadas()
        desc = input("Ingrese descripción: ")
        desc = desc if desc else registro.get_descripcion()
        id_proyecto = input("ID Proyecto: ")

        if id_proyecto:
            proyectoController = ProyectoController()
            proyecto = proyectoController.buscar_por_id(id_proyecto)
            if not proyecto:
                print("Proyecto no encontrado")
                return
            id_proyecto = int(id_proyecto)
        else:
            id_proyecto = registro.get_id_proyecto()

        id_empleado = input("Ingrese RUT del empleado: ")
        if not id_empleado:
            print("RUT no puede estar vacío")
            return

        if len(id_empleado.split("-")) != 2:
            print("El RUT debe tener un guión.")
            return

        if len(id_empleado.split("-")[0]) == 0:
            print("El RUT debe tener dígitos antes del verificador.")
            return

        if len(id_empleado.split("-")[1]) != 1:
            print("El RUT debe tener un dígito verificador.")
            return

        if id_empleado:
            empleadoController = EmpleadoController()
            empleado = empleadoController.buscar_por_rut(id_empleado)
            if not empleado:
                print("Empleado no encontrado.")
                return
            id_empleado = empleado[0]
        else:
            id_empleado = registro.get_id_empleado()

        nuevo_registro = RegistroTiempo(
            id=int(id_registro),
            descripcion=desc,
            fecha=fecha,
            horas_trabajadas=float(horas_trabajadas),
            id_empleado=int(id_empleado),
            id_proyecto=int(id_proyecto)
        )
        self.controller.modificar(nuevo_registro)

        print("Registro Modificado")

    def eliminar(self):
        id_registro = input("ID del Registro de tiempo a eliminar: ")

        if not self.controller.buscar_por_id(id_registro):
            print("Registro no encontrado.")
            return

        self.controller.eliminar(id_registro)
        print("Registro Eliminado.")
