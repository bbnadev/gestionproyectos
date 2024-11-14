from controllers.auth_controller import AuthController, Usuario


class AuthView:
    def __init__(self):
        self.controller = AuthController()

    def autenticar(self):
        try:
            usuario = input("Usuario: ")
            if len(usuario) < 1:
                raise ValueError(
                    "El usuario no puede estar vacío")
            if len(usuario) > 50:
                raise ValueError(
                    "El usuario no puede tener más de 50 caracteres")

            password = input("Contraseña: ")
            if len(password) < 1:
                raise ValueError(
                    "La contraseña no puede estar vacía")
            if len(password) > 255:
                raise ValueError(
                    "La contraseña no puede tener más de 255 caracteres")

            if self.controller.autenticar_usuario(usuario, password):
                print("Inicio de sesión exitoso.")
                return usuario
            else:
                print("Credenciales incorrectas.")
                return False
        except ValueError as ve:
            print(ve)

    def registrar(self):
        try:
            usuario = input("Nuevo usuario: ")
            if len(usuario) < 1:
                raise ValueError(
                    "El usuario no puede estar vacío")

            if len(usuario) > 50:
                raise ValueError(
                    "El usuario no puede tener más de 50 caracteres")

            password = input("Contraseña: ")
            if len(password) < 0:
                raise ValueError(
                    "La contraseña no puede estar vacía")
            if len(password) > 255:
                raise ValueError(
                    "La contraseña no puede tener más de 255 caracteres")

            self.controller.registrar_usuario(usuario, password)
            print("Usuario registrado exitosamente.")
        except ValueError as ve:
            print(ve)
