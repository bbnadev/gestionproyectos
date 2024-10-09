# models/empleado.py

class Empleado:
    def __init__(self, id=None, rut="", nombre="", direccion="", telefono="", email="", fecha_inicio=None, salario=0.0, departamento_id=None):
        self._id = id
        self._rut = rut
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._email = email
        self._fecha_inicio = fecha_inicio
        self._salario = salario
        self._departamento_id = departamento_id

    # Getters
    def get_id(self):
        return self._id

    def get_rut(self):
        return self._rut

    def get_nombre(self):
        return self._nombre

    def get_direccion(self):
        return self._direccion

    def get_telefono(self):
        return self._telefono

    def get_email(self):
        return self._email

    def get_fecha_inicio(self):
        return self._fecha_inicio

    def get_salario(self):
        return self._salario

    def get_departamento_id(self):
        return self._departamento_id

    # Setters
    def set_id(self, id):
        self._id = id

    def set_rut(self, rut):
        self._rut = rut

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_direccion(self, direccion):
        self._direccion = direccion

    def set_telefono(self, telefono):
        self._telefono = telefono

    def set_email(self, email):
        self._email = email

    def set_fecha_inicio(self, fecha_inicio):
        self._fecha_inicio = fecha_inicio

    def set_salario(self, salario):
        self._salario = salario

    def set_departamento_id(self, departamento_id):
        self._departamento_id = departamento_id