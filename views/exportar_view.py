import pandas as pd
from sqlalchemy import create_engine
from config.database import db_config


class ExportarView:
    def __init__(self):
        pass

    def exportar_excel(self):
        query = """
SELECT 
    e.id AS empleado_id,
    e.nombre AS empleado_nombre,
    e.rut AS empleado_rut,
    d.nombre AS departamento_nombre,
    p.nombre AS proyecto_nombre,
    rt.fecha AS fecha_registro,
    rt.horas_trabajadas,
    rt.descripcion AS descripcion_registro
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
        df_informe.to_excel('informes/informe_empleados.xlsx', index=False)
        print("Informe de Excel generado exitosamente.")
