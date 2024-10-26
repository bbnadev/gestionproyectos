from controllers.departamento_controller import DepartamentoController, Departamento


class DepartamentoView:
    def __init__(self):
        self.controller = DepartamentoController()

    def crear(self):
        nombre = input("Ingrese el nombre del departamento: ")
        if not nombre:
            print("El nombre del departamento no puede estar vacío.")
            return

        if self.controller.buscar_por_nombre(nombre):
            print("Ya existe un departamento con ese nombre.")
            return

        gerente_id = input("Ingrese el id del gerente (Opcional): ")
        gerente_id = int(gerente_id) if gerente_id else None

        nuevo_departamento = Departamento(nombre=nombre, gerente_id=gerente_id)
        id = self.controller.crear(nuevo_departamento)
        print("Departamento creado exitosamente con id:", id)

    def listar(self):
        departamentos = self.controller.listar()
        if not departamentos:
            print("No hay departamentos registrados.")
            return

        for departamento in departamentos:
            print(departamento)

    def buscar_por_id(self):
        id_departamento = input("Ingrese el id del departamento: ")
        if not id_departamento:
            print("El id del departamento no puede estar vacío.")
            return

        dept = self.controller.buscar_por_id(id_departamento)
        if not dept:
            print("Departamento no encontrado")
            return
        print(dept)

    def buscar_por_nombre(self):
        nombre_dept = input("Ingrese el nombre del departamento: ")
        if not nombre_dept:
            print("El nombre del departamento no puede estar vacío.")
            return
        dept = self.controller.buscar_por_nombre(nombre_dept)
        if not dept:
            print("Departamento no encontrado")
            return
        print(dept)

    def modificar(self):
        id_departamento = input("Ingrese el id del departamento a modificar: ")
        if not id_departamento:
            print("El id del departamento no puede estar vacío.")
            return
        dept = self.controller.buscar_por_id(id_departamento)
        if not dept:
            print("Departamento no encontrado")
            return

        dept = Departamento(*dept)
        nombre = input("Ingrese el nuevo nombre del departamento: ")
        if not nombre:
            nombre = dept.get_nombre()

        gerente_id = input("Ingrese el nuevo id del gerente (Opcional): ")
        if not gerente_id:
            gerente_id = dept.get_gerente_id()

        gerente_id = int(gerente_id) if gerente_id else None

        dept_modificado = Departamento(
            id=id_departamento, nombre=nombre, gerente_id=gerente_id)
        self.controller.modificar(dept_modificado)
        print("Departamento modificado exitosamente.")

    def eliminar(self):
        id_departamento = input("Ingrese el id del departamento a eliminar: ")
        if not id_departamento:
            print("El id del departamento no puede estar vacío.")
            return

        dept = self.controller.buscar_por_id(id_departamento)
        if not dept:
            print("Departamento no encontrado")
            return

        self.controller.eliminar(id_departamento)
        print("Departamento eliminado exitosamente.")
