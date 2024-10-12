from controllers.registro_tiempo_controller import RegistroTiempoController
from models.registro_tiempo import RegistroTiempo
from controllers.proyecto_controller import ProyectoController, Proyecto
from controllers.empleado_controller import EmpleadoController, Empleado


class RegistroTiempoView:
    def __init__(self):
        self.controller = RegistroTiempoController()

    def crear(self):
        proyectoController = ProyectoController()
        empleadoController = EmpleadoController()
    # fecha, horas_trabajadas, descripcion, id_empleado, id_proyecto
        rut_empleado = input("Ingrese el RUT del empleado: ")
        empleado = empleadoController.buscar_por_rut(rut_empleado)

        if not empleado:
            print("Empleado no encontrado")
            return

        id_proyecto = input("Ingrese el ID del Proyecto: ")
        proyecto = proyectoController.buscar_por_id(id_proyecto)

        if not proyecto:
            print("Proyecto no encontrado")
            return

        fecha = input("Ingrese la fecha: ")
        horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
        descripcion = input("Ingrese la descripción: ")

        nuevo_registro = RegistroTiempo(
            fecha=fecha,
            horas_trabajadas=horas_trabajadas,
            descripcion=descripcion,
            id_empleado=empleado[0],
            id_proyecto=int(id_proyecto)
        )

        id = self.controller.crear(nuevo_registro)
        print("Registro de tiempo creado con éxito con el ID:", id)
