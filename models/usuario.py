# models/usuario.py

class Usuario:
    def __init__(self, id=None, username: str = "", password_hash: str = ""):
        self._id = id
        self._username = username
        self._password_hash = password_hash

    # Getters y setters
    def get_id(self):
        return self._id

    def get_username(self):
        return self._username

    def get_password_hash(self):
        return self._password_hash

    def set_id(self, id):
        self._id = id

    def set_username(self, username):
        self._username = username

    def set_password_hash(self, password_hash):
        self._password_hash = password_hash
