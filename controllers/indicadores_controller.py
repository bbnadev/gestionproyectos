from models.indicador import Indicador
import mysql.connector
from config.database import db_config


class IndicadorController:
    def __init__(self):
        self.db_config = db_config

    def conectar(self):
        return mysql.connector.connect(**self.db_config)

    def crear(self, indicador: Indicador):
        conn = self.conectar()
        cursor = conn.cursor()
        query = "INSERT INTO Indicadores (nombre, valor, usuario, fecha_registro) VALUES (%s, %s, %s. %s)"
        cursor.execute(query, (indicador.get_nombre(),
                       indicador.get_valor(), indicador.get_usuario(), indicador.get_fecha_registro()))
        conn.commit()
        id = cursor.lastrowid
        cursor.close()
        conn.close()
        return id
    # TODO

# CREATE TABLE INDICADORES (
# 	id INT PRIMARY KEY AUTO_INCREMENT,
#     nombre varchar(25) NOT NULL,
#     valor INT NOT NULL,
#     usuario VARCHAR(255) NOT NULL,
# 	sitio VARCHAR(255) DEFAULT "mindicador.cl",
#     fecha_registro DATETIME NOT NULL,
#     fecha_consulta DATETIME DEFAULT CURRENT_TIMESTAMP
# )
