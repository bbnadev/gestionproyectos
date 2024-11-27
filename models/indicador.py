from datetime import datetime, date


class Indicador:
    # nombre del indicador, la fecha en que registra el valor, la fecha en que el usuario realiza la consulta, el usuario que la realiza y el sitio que provee los indicadores.
    def __init__(self, id=None, nombre="", fecha_registro=None, fecha_consulta=date.today(), valor=0.0, usuario="", sitio="mindicador.cl"):
        self._id = id
        self._nombre = nombre
        self._fecha_registro = fecha_registro
        self._fecha_consulta = fecha_consulta
        self._valor = valor
        self._usuario = usuario
        self._sitio = sitio

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_fecha_registro(self):
        return self._fecha_registro

    def get_fecha_consulta(self):
        return self._fecha_consulta

    def get_valor(self):
        return self._valor

    def get_usuario(self):
        return self._usuario

    def get_sitio(self):
        return self._sitio

    # Setters
    def set_id(self, id):
        self._id = id

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_fecha_registro(self, fecha_registro):
        self._fecha_registro = fecha_registro

    def set_fecha_consulta(self, fecha_consulta):
        self._fecha_consulta = fecha_consulta

    def set_valor(self, valor):
        self._valor = valor

    def set_usuario(self, usuario):
        self._usuario = usuario

    def set_sitio(self, sitio):
        self._sitio = sitio
