import mysql.connector
from models.registro_tiempo import RegistroTiempo
# Importa la configuración de la base de datos
from config.database import db_config


class RegistroTiempoController:
    def __init__(self):
        self.db_config = db_config  # Usa la configuración importada

    def conectar(self):
        return mysql.connector.connect(**self.db_config)

    def crear(self, registro_tiempo: RegistroTiempo):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "INSERT INTO RegistroTiempo (fecha, horas_trabajadas, descripcion, id_empleado, id_proyecto) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (registro_tiempo.get_fecha(), registro_tiempo.get_horas_trabajadas(
        ), registro_tiempo.get_descripcion(), registro_tiempo.get_id_empleado(), registro_tiempo.get_id_proyecto()))
        connection.commit()
        id = cursor.lastrowid
        cursor.close()
        connection.close()
        return id

    def listar(self):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "SELECT * FROM RegistroTiempo"
        cursor.execute(query)
        registros_tiempo = cursor.fetchall()
        cursor.close()
        connection.close()
        return registros_tiempo

    def buscar_por_id(self, id):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "SELECT * FROM RegistroTiempo WHERE id = %s"
        cursor.execute(query, (id,))
        registro_tiempo = cursor.fetchone()
        cursor.close()
        connection.close()
        return registro_tiempo

    def buscar_por_fecha(self, fecha):
        connection = self.conectar()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM RegistroTiempo WHERE fecha = '{fecha}'")
        registros_tiempo = cursor.fetchall()
        cursor.close()
        connection.close()
        return registros_tiempo

    def modificar(self, registro_tiempo: RegistroTiempo):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "UPDATE RegistroTiempo SET fecha = %s, horas_trabajadas = %s, descripcion = %s, id_empleado = %s, id_proyecto = %s WHERE id = %s"
        cursor.execute(query, (registro_tiempo.get_fecha(), registro_tiempo.get_horas_trabajadas(
        ), registro_tiempo.get_descripcion(), registro_tiempo.get_id_empleado(), registro_tiempo.get_id_proyecto(), registro_tiempo.get_id()))
        connection.commit()
        cursor.close()
        connection.close()

    def eliminar(self, id):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "DELETE FROM RegistroTiempo WHERE id = %s"
        cursor.execute(query, (id,))
        connection.commit()
        cursor.close()
        connection.close()

    # def buscar_por_id_empleado(self, id_empleado):
    #     connection = self.conectar()
    #     cursor = connection.cursor()
    #     cursor.execute(f"SELECT * FROM RegistroTiempo WHERE id_empleado = {id_empleado}")
    #     registros_tiempo = cursor.fetchall()
    #     cursor.close()
    #     connection.close()
    #     return registros_tiempo

    # def buscar_por_id_proyecto(self, id_proyecto):
    #     connection = self.conectar()
    #     cursor = connection.cursor()
    #     cursor.execute(f"SELECT * FROM RegistroTiempo WHERE id_proyecto = {id_proyecto}")
    #     registros_tiempo = cursor.fetchall()
    #     cursor.close()
    #     connection.close()
    #     return registros_tiempo

    # def buscar_por_id_empleado_proyecto(self, id_empleado, id_proyecto):
    #     connection = self.conectar()
    #     cursor = connection.cursor()
    #     cursor.execute(f"SELECT * FROM RegistroTiempo WHERE id_empleado = {id_empleado} AND id_proyecto = {id_proyecto}")
    #     registros_tiempo = cursor.fetchall()
    #     cursor.close()
    #     connection.close()
    #     return registros_tiempo

    # def buscar_por_fecha_id_empleado(self, fecha, id_empleado):
    #     connection = self.conectar()
    #     cursor = connection.cursor()
    #     cursor.execute(f"SELECT * FROM RegistroTiempo WHERE fecha = '{fecha}' AND id_empleado = {id_empleado}")
    #     registros_tiempo = cursor.fetchall()
    #     cursor.close()
    #     connection.close()
    #     return registros_tiempo

    # def buscar_por_fecha_id_proyecto(self, fecha, id_proyecto):
    #     connection = self.conectar()
    #     cursor = connection.cursor()
    #     cursor.execute(f"SELECT * FROM RegistroTiempo WHERE fecha = '{fecha}' AND id_proyecto = {id_proyecto}")
    #     registros_tiempo = cursor.fetchall()
    #     cursor.close()
    #     connection.close()
    #     return registros_tiempo

    # def buscar_por_fecha_id_empleado_proyecto(self, fecha, id_empleado, id_proyecto):
    #     connection = self.conectar()
    #     cursor = connection.cursor()
    #     cursor.execute(f"SELECT * FROM RegistroTiempo WHERE fecha = '{fecha}' AND id_empleado = {id_empleado} AND id_proyecto = {id_proyecto}")
    #     registros_tiempo = cursor.fetchall()
    #     cursor.close()
    #     connection.close()
    #     return registros_tiempo
