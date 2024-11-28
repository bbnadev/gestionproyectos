from controllers.indicadores_controller import IndicadorController, Indicador
from views.menu import menu_indicadores
import requests

from datetime import datetime, date
api = "https://mindicador.cl/api"


class IndicadoresView:
    def __init__(self):
        self.controller = IndicadorController()

    def consultar(self):
        while True:
            menu_indicadores()
            opcion = input("Seleccione una opción: ")
            match opcion:
                case "1":
                    info("uf")
                case "2":
                    info("ivp")
                case "3":
                    info("ipc")
                case "4":
                    info("utm")
                case "5":
                    info("dolar")
                case "6":
                    info("euro")
                case "q":
                    break

    def registrar(self, auth_user):
        while True:
            menu_indicadores()
            opcion = input("Seleccione una opción: ")
            match opcion:
                case "1":
                    fecha = input("Ingrese fecha (DD-MM-YYYY):")
                    fecha = fecha if fecha else date.today().strftime("%d-%m-%Y")
                    data: dict = requests.get(f'{api}/uf/{fecha}').json()

                    if data['message']:
                        print("ERROR:", data['message'])
                        break

                    if len(data['serie']) == 0:
                        print("No hay datos para la fecha ingresada")
                        break

                    indicador = Indicador(
                        nombre=data["codigo"],
                        fecha_registro=data['serie'][0]['fecha'][:10],
                        valor=data['serie'][0]['valor'],
                        usuario=auth_user,
                    )
                    id = self.controller.crear(indicador)
                    print(f"Registro del indicador \"UF\" creado con id #{id}")

                case "2":
                    fecha = input("Ingrese fecha (DD-MM-YYYY):")
                    fecha = fecha if fecha else date.today().strftime("%d-%m-%Y")
                    data: dict = requests.get(f'{api}/ivp/{fecha}').json()

                    if data['message']:
                        print("ERROR:", data['message'])
                        break

                    if len(data['serie']) == 0:
                        print("No hay datos para la fecha ingresada")
                        break

                    indicador = Indicador(
                        nombre=data["codigo"],
                        fecha_registro=data['serie'][0]['fecha'][:10],
                        valor=data['serie'][0]['valor'],
                        usuario=auth_user,
                    )
                    id = self.controller.crear(indicador)
                    print(
                        f"Registro del indicador \"IVP\" creado con id #{id}")

                case "3":
                    fecha = input("Ingrese fecha (DD-MM-YYYY):")
                    fecha = fecha if fecha else date.today().strftime("%d-%m-%Y")
                    data: dict = requests.get(f'{api}/ipc/{fecha}').json()

                    if data['message']:
                        print("ERROR:", data['message'])
                        break

                    if len(data['serie']) == 0:
                        print("No hay datos para la fecha ingresada")
                        break

                    indicador = Indicador(
                        nombre=data["codigo"],
                        fecha_registro=data['serie'][0]['fecha'][:10],
                        valor=data['serie'][0]['valor'],
                        usuario=auth_user,
                    )
                    id = self.controller.crear(indicador)
                    print(
                        f"Registro del indicador \"IPC\" creado con id #{id}")

                case "4":
                    fecha = input("Ingrese fecha (DD-MM-YYYY):")
                    fecha = fecha if fecha else date.today().strftime("%d-%m-%Y")
                    data: dict = requests.get(f'{api}/utm/{fecha}').json()

                    if data['message']:
                        print("ERROR:", data['message'])
                        break

                    if len(data['serie']) == 0:
                        print("No hay datos para la fecha ingresada")
                        break

                    indicador = Indicador(
                        nombre=data["codigo"],
                        fecha_registro=data['serie'][0]['fecha'][:10],
                        valor=data['serie'][0]['valor'],
                        usuario=auth_user,
                    )
                    id = self.controller.crear(indicador)
                    print(
                        f"Registro del indicador  \"UTM\" creado con id #{id}")

                case "5":
                    fecha = input("Ingrese fecha (DD-MM-YYYY):")
                    fecha = fecha if fecha else date.today().strftime("%d-%m-%Y")
                    data: dict = requests.get(f'{api}/dolar/{fecha}').json()

                    if data['message']:
                        print("ERROR:", data['message'])
                        break

                    if len(data['serie']) == 0:
                        print("No hay datos para la fecha ingresada")
                        break

                    indicador = Indicador(
                        nombre=data["codigo"],
                        fecha_registro=data['serie'][0]['fecha'][:10],
                        valor=data['serie'][0]['valor'],
                        usuario=auth_user,
                    )
                    id = self.controller.crear(indicador)
                    print(
                        f"Registro del indicador \"Dolar\" creado con id #{id}")
                case "6":
                    fecha = input("Ingrese fecha (DD-MM-YYYY):")
                    fecha = fecha if fecha else date.today().strftime("%d-%m-%Y")
                    data: dict = requests.get(f'{api}/euro/{fecha}').json()

                    if data['message']:
                        print("ERROR:", data['message'])
                        break

                    if len(data['serie']) == 0:
                        print("No hay datos para la fecha ingresada")
                        break

                    indicador = Indicador(
                        nombre=data["codigo"],
                        fecha_registro=data['serie'][0]['fecha'][:10],
                        valor=data['serie'][0]['valor'],
                        usuario=auth_user,
                    )
                    id = self.controller.crear(indicador)
                    print(
                        f"Registro del indicador \"Euro\" creado con id #{id}")

                case "q":
                    break


def info(indicador: str):

    data: dict = requests.get(f"{api}/{indicador}").json()
    print("\n")
    print("-"*50)
    print(f"Código: {data['codigo']}")
    print(f"Nombre: {data['nombre']}")
    print(f"Unidad de Medida: {data['unidad_medida']}")
    print(f"Fecha: {data['serie'][0]['fecha'][:10]}")
    print(f"Valor: {data['serie'][0]['valor']}")
    print("-"*50, "\n")
