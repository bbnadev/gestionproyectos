from controllers.departamento_controller import DepartamentoController
from models.departamento import Departamento


class DepartamentoView:
    def __init__(self):
        self.controller = DepartamentoController()

    def crear(self):
        nombre = input("Ingrese el nombre del departamento: ")
        gerente_id = input("Ingrese el id del gerente (Opcional): ")
        gerente_id = int(gerente_id) if gerente_id else None

        nuevo_departamento = Departamento(nombre=nombre, gerente_id=gerente_id)
        id = self.controller.crear(nuevo_departamento)
        print("Departamento creado exitosamente con id:", id)

    def listar(self):
        departamentos = self.controller.listar()
        for departamento in departamentos:
            print(departamento)

    def buscar_por_id(self):
        id_departamento = input("Ingrese el id del departamento: ")
        dept = self.controller.buscar_por_id(id_departamento)
        if not dept:
            print("Departamento no encontrado")
            return

        dept = Departamento(*dept)
        print(f"ID: {dept.get_id()}\nNombre: {
              dept.get_nombre()}\nID Gerente: {dept.get_gerente_id()}")

    def modificar(self):
        id_departamento = input("Ingrese el id del departamento a modificar: ")
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
        dept = self.controller.buscar_por_id(id_departamento)
        if not dept:
            print("Departamento no encontrado")
            return

        self.controller.eliminar(id_departamento)
        print("Departamento eliminado exitosamente.")
