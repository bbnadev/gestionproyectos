from models.indicador import Indicador
import mysql.connector
from config.database import db_config


class IndicadorController:
    def __init__(self):
        self.db_config = db_config

    def conectar(self):
        return mysql.connector.connect(**self.db_config)

    # TODO
    def crear(self):
        pass

    # TODO
