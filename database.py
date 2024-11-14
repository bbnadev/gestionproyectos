import mysql.connector
from config.database import db_config


class Database:
    def __init__(self):

        self.conn = mysql.connector.connect(**db_config)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()
