import pandas as pd
from controllers.exportar_controller import ExportarController

class ExportarView:
    def __init__(self):
        self.controller = ExportarController()

    def exportar_excel(self):

        df = self.controller.exportar()
        df.to_excel('informes/informe_empleados.xlsx', index=False)
        print("Informe de Excel generado exitosamente.")

    def exportar_pdf(self):
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_pdf import PdfPages

        df = self.controller.exportar()

        fig, ax = plt.subplots(figsize=(16.5, 11.7))
        # A3 = 11.7 x 16.5 inches
        # A4 = 8.3 x 11.7 inches
        ax.axis('tight')
        ax.axis('off')
        ax.table(cellText=df.values,
                 colLabels=df.columns, loc="center")
        ax.set_title('Informe de empleados')

        pp = PdfPages("informes/informe_empleados.pdf")
        pp.savefig(fig, bbox_inches='tight')
        pp.close()
        print("Informe de PDF generado exitosamente.")
