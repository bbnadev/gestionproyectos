# controllers/empleado_controller.py
import mysql.connector
from models.empleado import Empleado
from config.database import db_config  # Importa la configuración de la base de datos

class EmpleadoController:
    def __init__(self):
        self.db_config = db_config  # Usa la configuración importada

    def conectar(self):
        return mysql.connector.connect(**self.db_config)

    def crear_empleado(self, empleado):
        connection = self.conectar()
        cursor = connection.cursor()
        query = ("INSERT INTO Empleado (rut, nombre, direccion, telefono, email, fecha_inicio, salario, departamento_id) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
        cursor.execute(query, (empleado.get_rut(), empleado.get_nombre(), empleado.get_direccion(),
                               empleado.get_telefono(), empleado.get_email(), empleado.get_fecha_inicio(),
                               empleado.get_salario(), empleado.get_departamento_id()))
        connection.commit()
        cursor.close()
        connection.close()

    # Los demás métodos CRUD seguirían aquí...

    def listar_empleados(self):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "SELECT * FROM Empleado"
        cursor.execute(query)
        empleados = cursor.fetchall()
        cursor.close()
        connection.close()
        return empleados

    def buscar_empleado_por_rut(self, rut):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "SELECT * FROM Empleado WHERE rut = %s"
        cursor.execute(query, (rut,))
        empleado = cursor.fetchone()
        cursor.close()
        connection.close()
        return empleado

    def modificar_empleado(self, empleado):
        connection = self.conectar()
        cursor = connection.cursor()
        query = ("UPDATE Empleado SET nombre = %s, direccion = %s, telefono = %s, email = %s, "
                 "fecha_inicio = %s, salario = %s, departamento_id = %s WHERE rut = %s")
        cursor.execute(query, (empleado.get_nombre(), empleado.get_direccion(),
                               empleado.get_telefono(), empleado.get_email(), empleado.get_fecha_inicio(),
                               empleado.get_salario(), empleado.get_departamento_id(), empleado.get_rut()))
        connection.commit()
        cursor.close()
        connection.close()

    def eliminar_empleado(self, rut):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "DELETE FROM Empleado WHERE rut = %s"
        cursor.execute(query, (rut,))
        connection.commit()
        cursor.close()
        connection.close()