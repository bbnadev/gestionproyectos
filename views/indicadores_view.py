from controllers.indicadores_controller import IndicadorController, Indicador

import requests

from datetime import datetime, date
api = "https://mindicador.cl/api/"


class IndicadoresView:
    def __init__(self):
        self.controller = IndicadorController()

    # TODO
    """
     Consulta de Indicadores Económicos: 
    El sistema debe permitir consultar indicadores económicos, para ello se requiere poder seleccionar el indicador económico e ingresar una fecha determinada para obtener el valor del indicador o un periodo entre dos fechas obteniendo como resultado el listado de valores del periodo consultado. Los indicadores económicos requeridos para el listado son: Unidad de Fomento (UF), Índice de valor Promedio (IVP), Índice de Precio al Consumidor (IPC), Unidad Tributaria Mensual (UTM), Dólar Observado, Euro. 
    """

    def consultar(self):
        while True:

            # Unidad de Fomento (UF), Índice de valor Promedio (IVP), Índice de Precio al Consumidor (IPC), Unidad Tributaria Mensual (UTM), Dólar Observado, Euro. 

            # data: dict = requests.get(api).json()
            # i = 0
            # for _, value in data.items():
            #     if isinstance(value, dict):
            #         i += 1
            #         print(f"{f"{i}.": >3} {value['nombre']}")
            print("1. Unidad de Fomento (UF)")
            print("2. Índice de valor Promedio (IVP)")
            print("3. Índice de Precio al Consumidor (IPC)")
            print("4. Unidad Tributaria Mensual (UTM)")
            print("5. Dólar Observado")
            print("6. Euro")
            print("q. Salir")
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

    """
    Registro de indicadores Económicos:
    La empresa debe registrar los datos consultados cuando el usuario lo requiera, para ello deberá almacenar en la base de datos el nombre del indicador, la fecha en que registra el valor, la fecha en que el usuario realiza la consulta, el usuario que la realiza y el sitio que provee los indicadores.
    - Base de datos
        - Nombre del indicador
        - Fecha de registro
        - Fecha de consulta
        - Usuario
        - Sitio web
    """

    def registrar(self, auth_user):
            while True:
                print("1. Unidad de Fomento (UF)")
                print("2. Índice de valor Promedio (IVP)")
                print("3. Índice de Precio al Consumidor (IPC)")
                print("4. Unidad Tributaria Mensual (UTM)")
                print("5. Dólar Observado")
                print("6. Euro")
                print("q. Salir")
                opcion = input("Seleccione una opción: ")
                match opcion:
                    case "1":
                        fecha = input("Ingrese fecha (DD-MM-YYYY):")
                        fecha = fecha if fecha else date.today().strftime("%d-%m-%Y")
                        data: dict = requests.get(f'{api}uf/{fecha}').json()
                        indicador = Indicador(
                            nombre=data["codigo"],
                            fecha_registro=data['serie'][0]['fecha'][:10],
                            valor=data['serie'][0]['valor'],
                            usuario=auth_user,
                        )
                        id = self.controller.crear(indicador)
                        print(f"registro creado con id", id)
                    case "2":
                        fecha = input("Ingrese fecha (DD-MM-YYYY):")
                        fecha = fecha if fecha else date.today().strftime("%d-%m-%Y")
                        data: dict = requests.get(f'{api}ivp/{fecha}').json()
                        indicador = Indicador(
                            nombre=data["codigo"],
                            fecha_registro=data['serie'][0]['fecha'][:10],
                            valor=data['serie'][0]['valor'],
                            usuario=auth_user,
                        )
                        id = self.controller.crear(indicador)
                        print(f"registro creado con id", id)
                    case "3":
                        fecha = input("Ingrese fecha (DD-MM-YYYY):")
                        fecha = fecha if fecha else date.today().strftime("%d-%m-%Y")
                        data: dict = requests.get(f'{api}ipc/{fecha}').json()
                        indicador = Indicador(
                            nombre=data["codigo"],
                            fecha_registro=data['serie'][0]['fecha'][:10],
                            valor=data['serie'][0]['valor'],
                            usuario=auth_user,
                        )
                        id = self.controller.crear(indicador)
                        print(f"registro creado con id", id)
                    case "4":
                        fecha = input("Ingrese fecha (DD-MM-YYYY):")
                        fecha = fecha if fecha else date.today().strftime("%d-%m-%Y")
                        data: dict = requests.get(f'{api}utm/{fecha}').json()
                        indicador = Indicador(
                            nombre=data["codigo"],
                            fecha_registro=data['serie'][0]['fecha'][:10],
                            valor=data['serie'][0]['valor'],
                            usuario=auth_user,
                        )
                        id = self.controller.crear(indicador)
                        print(f"registro creado con id", id)
                    case "5":
                        indicador = Indicador(
                            nombre=data["codigo"],
                            fecha_registro=data['serie'][0]['fecha'][:10],
                            valor=data['serie'][0]['valor'],
                            usuario=auth_user,
                        )
                        self.controller.crear(indicador)
                        fecha = input("Ingrese fecha (DD-MM-YYYY):")
                        fecha = fecha if fecha else date.today().strftime("%d-%m-%Y")
                        data: dict = requests.get(f'{api}dolar/{fecha}').json()
                        indicador = Indicador(
                            nombre=data["codigo"],
                            fecha_registro=data['serie'][0]['fecha'][:10],
                            valor=data['serie'][0]['valor'],
                            usuario=auth_user,
                        )
                        id = self.controller.crear(indicador)
                        print(f"registro creado con id", id)
                    case "6":
                        fecha = input("Ingrese fecha (DD-MM-YYYY):")
                        fecha = fecha if fecha else date.today().strftime("%d-%m-%Y")
                        data: dict = requests.get(f'{api}euro/{fecha}').json()

                        indicador = Indicador(
                            nombre=data["codigo"],
                            fecha_registro=data['serie'][0]['fecha'][:10],
                            valor=data['serie'][0]['valor'],
                            usuario=auth_user,
                        )
                        id = self.controller.crear(Indicador(indicador))
                        print(f"registro creado con id", id)
                    case "q":
                        break
        


def info(indicador: str):

    # if fecha:
    #     data: dict = requests.get(f'{api}{indicador}/{fecha}').json()
    #     return data
    #     # return {
    #     #     "codigo": data["codigo"],
    #     #     "nombre": data["nombre"],
    #     #     "unidad_medida": data["unidad_medida"],
    #     #     "fecha": data['serie'][0]['fecha'][:10],
    #     #     "valor": data['serie'][0]['valor']
    #     # }

    # else:
        data: dict = requests.get(api + indicador).json()
        print(data)
        print("\n")
        print("-"*50)
        print(f"Código: {data['codigo']}")
        print(f"Nombre: {data['nombre']}")
        print(f"Unidad de Medida: {data['unidad_medida']}")
        print(f"Fecha: {data['serie'][0]['fecha'][:10]}")
        print(f"Valor: {data['serie'][0]['valor']}")
        print("-"*50, "\n")
