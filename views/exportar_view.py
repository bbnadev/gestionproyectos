import pandas as pd
from sqlalchemy import create_engine
from config.database import db_config
from datetime import date

class ExportarView:
    def __init__(self):
        pass

    def exportar_excel(self):
        query = """
SELECT 
    e.id AS ID,
    e.nombre AS NOMBRE,
    e.rut AS RUT,
    d.nombre AS DEPARTAMENTO,
    p.nombre AS PROYECTO,
    rt.fecha AS "FECHA REGISTRO",
    rt.horas_trabajadas AS "HORAS TRABAJADAS",
    rt.descripcion AS "DESCRIPCIÓN"
FROM 
    empleado e
LEFT JOIN 
    departamento d ON e.departamento_id = d.id
LEFT JOIN 
    RegistroTiempo rt ON e.id = rt.id_empleado
LEFT JOIN 
    Proyecto p ON rt.id_proyecto = p.id
"""

        db_connection_str = f'mysql+mysqlconnector://{db_config['user']}:{
            db_config['password']}@{db_config['host']}/{db_config["database"]}'
        db_connection = create_engine(db_connection_str)

        df_informe = pd.read_sql(
            query, con=db_connection)
        df_informe.to_excel(f'informes/informe_empleados_{date.today()}.xlsx', index=False)
        print("Informe de Excel generado exitosamente.")
