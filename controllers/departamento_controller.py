# controllers/departamento_controller.py

import mysql.connector
from models.departamento import Departamento
from config.database import db_config


class DepartamentoController:
    def __init__(self):
        self.db_config = db_config

    def conectar(self):
        return mysql.connector.connect(**self.db_config)

    def crear(self, departamento: Departamento):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "INSERT INTO Departamento (nombre, gerente_id) VALUES (%s, %s)"
        cursor.execute(query, (departamento.get_nombre(),
                       departamento.get_gerente_id()))
        connection.commit()
        id = cursor.lastrowid
        cursor.close()
        connection.close()
        return id

    def listar(self):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "SELECT * FROM Departamento"
        cursor.execute(query)
        departamentos = cursor.fetchall()
        cursor.close()
        connection.close()
        return departamentos

    def buscar_por_id(self, id: int):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "SELECT * FROM Departamento WHERE id = %s"
        cursor.execute(query, (id,))
        departamento = cursor.fetchone()
        cursor.close()
        connection.close()
        return departamento

    def modificar(self, departamento: Departamento):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "UPDATE Departamento SET nombre = %s, gerente_id = %s WHERE id = %s"
        cursor.execute(query, (departamento.get_nombre(),
                       departamento.get_gerente_id(), departamento.get_id()))
        connection.commit()
        cursor.close()
        connection.close()

    def eliminar(self, id: int):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "DELETE FROM Departamento WHERE id = %s"
        cursor.execute(query, (id,))
        connection.commit()
        cursor.close()
        connection.close()
