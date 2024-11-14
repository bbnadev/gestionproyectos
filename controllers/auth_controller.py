import bcrypt
from models.usuario import Usuario
import mysql.connector
from config.database import db_config


class AuthController:
    def __init__(self):
        self.db_config = db_config

    def conectar(self):
        return mysql.connector.connect(**self.db_config)

    def registrar_usuario(self, usuario, password):
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        usuario = Usuario(username=usuario, password_hash=hashed)
        connection = self.conectar()
        cursor = connection.cursor()

        query = "INSERT INTO Usuario (username, password_hash) VALUES (%s, %s)"

        cursor.execute(query, (usuario.get_username(), hashed))
        connection.commit()
        cursor.close()
        connection.close()

    def autenticar_usuario(self, usuario, password):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "SELECT password_hash FROM Usuario WHERE username = %s"
        cursor.execute(query, (usuario,))
        usuario = cursor.fetchone()
        if usuario:
            return bcrypt.checkpw(password.encode('utf-8'), usuario[0].encode('utf-8'))
        return False
