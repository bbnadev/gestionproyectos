class RegistroTiempo:
    def __init__(self, id=None, fecha=None, horas_trabajadas=0.0, descripcion="", id_empleado=None, id_proyecto=None):
        self._id = id
        self._fecha = fecha
        self._horas_trabajadas = horas_trabajadas
        self._descripcion = descripcion
        self._id_empleado = id_empleado
        self._id_proyecto = id_proyecto

    def get_id(self):
        return self._id

    def get_fecha(self):
        return self._fecha

    def get_horas_trabajadas(self):
        return self._horas_trabajadas

    def get_descripcion(self):
        return self._descripcion

    def get_id_empleado(self):
        return self._id_empleado

    def get_id_proyecto(self):
        return self._id_proyecto

    def set_id(self, id):
        self._id = id

    def set_fecha(self, fecha):
        self._fecha = fecha

    def set_horas_trabajadas(self, horas_trabajadas):
        self._horas_trabajadas = horas_trabajadas

    def set_descripcion(self, descripcion):
        self._descripcion = descripcion

    def set_id_empleado(self, id_empleado):
        self._id_empleado = id_empleado

    def set_id_proyecto(self, id_proyecto):
        self._id_proyecto = id_proyecto
