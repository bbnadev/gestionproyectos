# Modelo Proyecto
class Proyecto:
    def __init__(self, id=None, nombre="", descripcion="", fecha_inicio=None, empleados=[]):
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion
        self._fecha_inicio = fecha_inicio
        self._empleados = empleados

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_descripcion(self):
        return self._descripcion

    def get_fecha_inicio(self):
        return self._fecha_inicio

    def get_fecha_inicio(self):
        return self._empleados

    # Setters

    def set_id(self, id):
        self._id = id

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_descripcion(self, descripcion):
        self._descripcion = descripcion

    def set_fecha_inicio(self, fecha_inicio):
        self._fecha_inicio = fecha_inicio

    def add_empleados(self, empleado):
        self._empleados.append(empleado)

    def remove_empleados(self, empleado):
        self._empleados.remove(empleado)
