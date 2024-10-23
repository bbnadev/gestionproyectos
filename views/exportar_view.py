import pandas as pd
from sqlalchemy import create_engine
from config.database import db_config


class ExportarView:
    def __init__(self):
        self._query = """
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
        self._connector_str = f'mysql+mysqlconnector://{db_config['user']}:{
            db_config['password']}@{db_config['host']}/{db_config["database"]}'

    def query(self):
        return self._query

    def get_connector_str(self):
        return self._connector_str

    def create_connection(self):
        db_connection_str = self.get_connector_str()
        db_connection = create_engine(db_connection_str)
        return db_connection

    def exportar_excel(self):

        conn = self.create_connection()

        df = pd.read_sql(
            self.query(), con=conn)
        df.to_excel('informes/informe_empleados.xlsx', index=False)
        print("Informe de Excel generado exitosamente.")

    def exportar_pdf(self):
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_pdf import PdfPages

        conn = self.create_connection()

        df = pd.read_sql(
            self.query(), con=conn)

        fig, ax = plt.subplots(figsize=(12, 4))
        ax.axis('tight')
        ax.axis('off')
        ax.table(cellText=df.values,
                 colLabels=df.columns)
        ax.set_title('Informe de empleados')

        pp = PdfPages("informes/informe_empleados.pdf")
        pp.savefig(fig, bbox_inches='tight')
        pp.close()
        print("Informe de PDF generado exitosamente.")
