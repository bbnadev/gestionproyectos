# models/departamento.py

class Departamento:
    def __init__(self, id=None, nombre="", gerente_id=None):
        self._id = id
        self._nombre = nombre
        self._gerente_id = gerente_id

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_gerente_id(self):
        return self._gerente_id

    # Setters
    def set_id(self, id):
        self._id = id

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_gerente_id(self, gerente_id):
        self._gerente_id = gerente_id
