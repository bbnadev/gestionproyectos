from controllers.empleado_controller import EmpleadoController
from models.empleado import Empleado


class EmpleadoView:
    def __init__(self):
        self.controller = EmpleadoController()

    def crear(self):
        rut = input("Ingrese el RUT del empleado: ")

        if self.controller.buscar_por_rut(rut):
            print("Ya existe un empleado con ese RUT.")
            return

        nombre = input("Ingrese el nombre del empleado: ")
        direccion = input("Ingrese la dirección del empleado: ")
        telefono = input("Ingrese el teléfono del empleado: ")
        email = input("Ingrese el email del empleado: ")
        fecha_inicio = input(
            "Ingrese la fecha de inicio del empleado (YYYY-MM-DD): ")
        salario = float(input("Ingrese el salario del empleado: "))
        departamento_id = int(
            input("Ingrese el ID del departamento del empleado: "))
        nuevo_empleado = Empleado(
            rut=rut,
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            email=email,
            fecha_inicio=fecha_inicio,
            salario=salario,
            departamento_id=departamento_id
        )
        self.controller.crear(nuevo_empleado)
        print("Empleado creado exitosamente.")

    def listar(self):
        empleados = self.controller.listar()
        for empleado in empleados:
            print(empleado)

    def buscar_por_rut(self):
        rut = input("Ingrese el RUT del empleado a buscar: ")
        empleado = self.controller.buscar_por_rut(rut)
        if not empleado:
            print("Empleado no encontrado.")
            return
        print(empleado)

    def buscar_por_id(self):
        id_empleado = input("Ingrese el ID del empleado a buscar: ")
        empleado = self.controller.buscar_por_id(id_empleado)
        if not empleado:
            print("Empleado no encontrado.")
            return
        print(empleado)

    def modificar(self):
        rut = input("Ingrese el RUT del empleado a modificar: ")
        empleado = self.controller.buscar_por_rut(rut)
        if not empleado:
            print("Empleado no encontrado.")
            return

        empleado = Empleado(*empleado)
        nombre = input("Ingrese el nombre: ")
        if not nombre:
            nombre = empleado.get_nombre()

        direccion = input("Ingrese la dirección: ")
        if not direccion:
            direccion = empleado.get_direccion()

        telefono = input("Ingrese el nuevo teléfono: ")
        if not telefono:
            telefono = empleado.get_telefono()

        email = input("Ingrese el email: ")
        if not email:
            email = empleado.get_email()

        fecha_inicio = input(
            "Ingrese fecha de inicio del empleado (YYYY-MM-DD): ")
        if not fecha_inicio:
            fecha_inicio = empleado.get_fecha_inicio()

        salario = input("Ingrese el nuevo salario del empleado: ")
        if not salario:
            salario = empleado.get_salario()
        departamento_id = input(
            "Ingrese el nuevo ID del departamento del empleado: ")
        if not departamento_id:
            departamento_id = empleado.get_departamento_id()

        empleado_modificado = Empleado(
            rut=rut,
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            email=email,
            fecha_inicio=fecha_inicio,
            salario=float(salario),
            departamento_id=int(departamento_id)
        )
        self.controller.modificar(empleado_modificado)
        print("Empleado modificado exitosamente.")

    def eliminar(self):
        rut = input("Ingrese el RUT del empleado a eliminar: ")
        empleado = self.controller.buscar_por_rut(rut)
        if not empleado:
            print("Empleado no encontrado.")
            return
        self.controller.eliminar(rut)
        print("Empleado eliminado exitosamente.")
