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
            data: dict = requests.get(api).json()
            i = 0
            for _, value in data.items():
                if isinstance(value, dict):
                    i += 1
                    print(f"{f"{i}.": >3} {value['nombre']}")
            print(f"{f"q.": >3} Salir")
            opcion = input("Seleccione una opción: ")
            match opcion:
                case "1":
                    info("uf")
                case "2":
                    info("ivp")
                case "3":
                    info("dolar")
                case "4":
                    info("dolar_intercambio")
                case "5":
                    info("euro")
                case "6":
                    info("ipc")
                case "7":
                    info("utm")
                case "8":
                    info("imacec")
                case "9":
                    info("tpm")
                case "10":
                    info("libra_cobre")
                case "11":
                    info("tasa_desempleo")
                case "12":
                    info("bitcoin")
                case "q":
                    break


def info(indicador: str):
    data: dict = requests.get(api + indicador).json()
    print("-"*50)
    print(f"Código: {data['codigo']}")
    print(f"Nombre: {data['nombre']}")
    print(f"Unidad de Medida: {data['unidad_medida']}")
    print(f"Fecha: {data['serie'][0]['fecha'][:10]}")
    print(f"Valor: {data['serie'][0]['valor']}")
    print("-"*50, "\n")

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

    def registrar(self):
