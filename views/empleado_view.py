from controllers.empleado_controller import EmpleadoController, Empleado
from controllers.departamento_controller import DepartamentoController


class EmpleadoView:
    def __init__(self):
        self.controller = EmpleadoController()

    def crear(self):
        rut = input("Ingrese el RUT del empleado: ")
        if self.controller.buscar_por_rut(rut):
            print("Ya existe un empleado con ese RUT.")
            return

        if len(rut.split("-")) != 2:
            print("El RUT debe tener un guión.")
            return

        if len(rut.split("-")[1]) != 1:
            print("El RUT debe tener un dígito verificador.")
            return

        nombre = input("Ingrese el nombre del empleado: ")
        if not nombre:
            print("El nombre es requerido.")
            return

        direccion = input("Ingrese la dirección del empleado: ")
        if not direccion:
            print("La dirección es requerida.")
            return

        telefono = input("Ingrese el teléfono del empleado: ")
        if not telefono:
            print("El teléfono es requerido.")
            return

        email = input("Ingrese el email del empleado: ")
        if not email:
            print("El email es requerido.")
            return

        fecha_inicio = input(
            "Ingrese la fecha de inicio del empleado (YYYY-MM-DD): ")
        if not fecha_inicio:
            print("La fecha de inicio es requerida.")
            return

        salario = input("Ingrese el salario del empleado: ")
        if not salario:
            print("El salario es requerido.")
            return

        dept_id = input("Ingrese el ID del departamento del empleado: ")
        if not dept_id:
            print("El ID del departamento es requerido.")
            return

        deptController = DepartamentoController()
        if not deptController.buscar_por_id(int(dept_id)):
            print("No existe un departamento con ese ID.")
            return

        nuevo_empleado = Empleado(
            rut=rut,
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            email=email,
            fecha_inicio=fecha_inicio,
            salario=float(salario),
            departamento_id=int(dept_id)
        )
        self.controller.crear(nuevo_empleado)
        print("Empleado creado exitosamente.")

    def listar(self):
        empleados = self.controller.listar()
        if not empleados:
            print("No hay empleados registrados.")
            return

        for empleado in empleados:
            print(empleado)

    def buscar_por_rut(self):
        rut = input("Ingrese el RUT del empleado a buscar: ")
        if not rut:
            print("El RUT es requerido.")
            return

        if len(rut.split("-")) != 2:
            print("El RUT debe tener un guión.")
            return

        if len(rut.split("-")[1]) != 1:
            print("El RUT debe tener un dígito verificador.")
            return

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

        if not rut:
            print("El RUT es requerido.")
            return

        if len(rut.split("-")) != 2:
            print("El RUT debe tener un guión.")
            return

        if len(rut.split("-")[1]) != 1:
            print("El RUT debe tener un dígito verificador.")
            return

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
        if not rut:
            print("El RUT es requerido.")
            return

        if len(rut.split("-")) != 2:
            print("El RUT debe tener un guión.")
            return

        if len(rut.split("-")[1]) != 1:
            print("El RUT debe tener un dígito verificador.")
            return

        empleado = self.controller.buscar_por_rut(rut)
        if not empleado:
            print("Empleado no encontrado.")
            return
        self.controller.eliminar(rut)
        print("Empleado eliminado exitosamente.")
