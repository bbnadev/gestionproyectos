from controllers.indicadores_controller import IndicadorController, Indicador

import requests


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
            print("1. Unidad de Fomento (UF)")
            print("2. Índice de valor Promedio (IVP)")
            print("3. Índice de Precio al Consumidor (IPC)")
            print("4. Unidad Tributaria Mensual (UTM)")
            print("5. Dólar Observado")
            print("6. Euro")
            print("q. Salir")
            opcion = input("Seleccione una opción: ")
            # match opcion:
            #     case "1":
            #         info("uf")
            #     case "2":
            #         info("ivp")
            #     case "3":
            #         info("ipc")
            #     case "4":
            #         info("utm")
            #     case "5":
            #         info("dolar")
            #     case "6":
            #         info("euro")
            #     case "q":
            #         break
                

            # fecha_registro = input("Ingrese la fecha de registro del indicador: ")

            # data: dict = requests.get(api + id_indicador).json()

            # fechas: list = data['serie']
            # index = 0
            # for item in fechas:
            #     if item['fecha'][:10] == fecha_registro:
            #         index = fechas.index(item)

            # indicador = Indicador(
            #     nombre=data['nombre'],
            #     fecha_registro=fecha_registro,
            #     valor=fechas[index]['valor'],
            #     usuario=auth_user,
            # )
            # TODO guardar en base de datos


def info(indicador: str):
    data: dict = requests.get(api + indicador).json()
    print("\n")
    print("-"*50)
    print(f"Código: {data['codigo']}")
    print(f"Nombre: {data['nombre']}")
    print(f"Unidad de Medida: {data['unidad_medida']}")
    print(f"Fecha: {data['serie'][0]['fecha'][:10]}")
    print(f"Valor: {data['serie'][0]['valor']}")
    print("-"*50, "\n")
