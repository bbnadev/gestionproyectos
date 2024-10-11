from models.proyecto import Proyecto
from config.database import db_config
import mysql.connector


class ProyectoController:
    def __init__(self):
        self.db_config = db_config

    def conectar(self):
        return mysql.connector.connect(**self.db_config)

    def crear(self, proyecto: Proyecto):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "INSERT INTO Proyecto (nombre, descripcion, fecha_inicio) VALUES (%s, %s, %s)"
        cursor.execute(query, (proyecto.get_nombre(),
                       proyecto.get_descripcion(), proyecto.get_fecha_inicio()))
        connection.commit()
        id = cursor.lastrowid
        cursor.close()
        connection.close()
        return id

    def listar(self):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "SELECT * FROM Proyecto"
        cursor.execute(query)
        proyectos = cursor.fetchall()
        cursor.close()
        connection.close()
        return proyectos

    def buscar_por_id(self, id):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "SELECT * FROM Proyecto WHERE id = %s"
        cursor.execute(query, (id,))
        proyecto = cursor.fetchone()
        cursor.close()
        connection.close()
        return proyecto

    def buscar_por_nombre(self, nombre):
        connection = self.conectar()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM Proyecto WHERE nombre LIKE '{nombre}%'")
        proyecto = cursor.fetchone()
        cursor.close()
        connection.close()
        return proyecto

    def modificar(self, proyecto: Proyecto):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "UPDATE Proyecto SET nombre = %s, descripcion = %s, fecha_inicio = %s WHERE id = %s"
        cursor.execute(query, (proyecto.get_nombre(), proyecto.get_descripcion(
        ), proyecto.get_fecha_inicio(), proyecto.get_id()))
        connection.commit()
        cursor.close()
        connection.close()

    def eliminar(self, id):
        connection = self.conectar()
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM Proyecto WHERE id = {id}")
        connection.commit()
        cursor.close()
        connection.close()

    def agregar_empleado(self, id_proyecto, id_empleado):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "INSERT INTO ProyectoXEmpleado (id_proyecto, id_empleado) VALUES (%s, %s)"
        cursor.execute(query, (id_proyecto, id_empleado))
        connection.commit()
        cursor.close()
        connection.close()

    def quitar_empleado(self, id_proyecto, id_empleado):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "DELETE FROM ProyectoXEmpleado WHERE id_proyecto = %s AND id_empleado = %s"
        cursor.execute(query, (id_proyecto, id_empleado))
        connection.commit()
        cursor.close()
        connection.close()

    def listar_empleados(self, id_proyecto):
        connection = self.conectar()
        cursor = connection.cursor()
        cursor.execute(
            f"SELECT e.id id, e.rut rut, e.nombre nombre, e.direccion direccion, e.telefono telefono, e.email email, e.fecha_inicio fecha_inicio, e.salario salario, e.departamento_id departamento_id FROM ProyectoXEmpleado PxE JOIN Proyecto p ON PxE.id_proyecto = p.id JOIN Empleado e ON PxE.id_empleado = e.id WHERE id_proyecto = {id_proyecto}")
        empleados = cursor.fetchall()
        cursor.close()
        connection.close()
        return empleados
