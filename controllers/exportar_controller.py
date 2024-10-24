from sqlalchemy import create_engine
from config.database import db_config
import pandas as pd
class ExportarController:
    def __init__(self):
        self.db_config = db_config

    def conectar(self):
        return create_engine(f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config["database"]}")
    
    def exportar(self):
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
        return pd.read_sql(query, con=self.conectar())
