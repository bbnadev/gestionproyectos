import bcrypt
from models.usuario import Usuario
from database import Database


class AuthController:
    def __init__(self):
        self.db = Database()

    def registrar_usuario(self, usuario, password):
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        usuario = Usuario(username=usuario, password_hash=hashed)
        query = "INSERT INTO Usuario (username, password_hash) VALUES (%s, %s)"
        self.db.cursor.execute(query, (usuario.get_username(), hashed))
        self.db.conn.commit()
        self.db.close()

    def autenticar_usuario(self, usuario, password):
        query = "SELECT password_hash FROM Usuario WHERE username = %s"
        self.db.cursor.execute(query, (usuario,))
        usuario = self.db.cursor.fetchone()
        if usuario:
            return bcrypt.checkpw(password.encode('utf-8'), usuario[0].encode('utf-8'))
        return False
