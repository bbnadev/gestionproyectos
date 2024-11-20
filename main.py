# main.py
from views.menu import menu_principal, menu_empleado, menu_departamento, menu_proyecto, menu_registro_tiempo, menu_exportar, menu_indicadores_economicos, menu_inicio
from views.proyecto_view import ProyectoView
from views.empleado_view import EmpleadoView
from views.departamento_view import DepartamentoView
from views.registro_tiempo_view import RegistroTiempoView
from views.exportar_view import ExportarView
from views.auth_view import AuthView
from views.indicadores_view import IndicadoresView

# def limpiar_consola():
#     import os
#     os.system("cls" if os.name == "nt" else "clear")


def main():
    usuario_actual = None
    while True:
        if not usuario_actual:
            menu_inicio()
            authView = AuthView()
            # opt = msvcrt.getch().decode('utf-8').lower()
            opt = input("Seleccione una opción: ")
            match opt:
                case "1":
                    usuario_actual = authView.autenticar()
                case "2":
                    authView.registrar()
                case "q":
                    break
        else:
            menu_principal()
            opcion = input("Seleccione una opción: ")
            match opcion:
                case "1":
                    empleado_view = EmpleadoView()
                    while True:
                        menu_empleado()
                        sub_opcion = input("Seleccione una opción: ")
                        match sub_opcion:
                            case "1.1":
                                empleado_view.crear()
                            case "1.2":
                                empleado_view.listar()
                            case "1.3":
                                empleado_view.buscar_por_rut()
                            case "1.4":
                                empleado_view.buscar_por_id()
                            case "1.5":
                                empleado_view.modificar()
                            case "1.6":
                                empleado_view.eliminar()
                            case "q":
                                break
                case "2":
                    dept_view = DepartamentoView()
                    while True:
                        menu_departamento()
                        sub_opcion = input("Seleccione una opción: ")
                        match sub_opcion:
                            case "2.1":
                                dept_view.crear()
                            case "2.2":
                                dept_view.listar()
                            case "2.3":
                                dept_view.buscar_por_id()
                            case "2.4":
                                dept_view.buscar_por_nombre()
                            case "2.5":
                                dept_view.modificar()
                            case "2.6":
                                dept_view.eliminar()
                            case "q":
                                break

                case "3":
                    proyecto_view = ProyectoView()
                    while True:
                        menu_proyecto()
                        sub_opcion = input("Seleccione una opción: ")
                        match sub_opcion:
                            case "3.1":
                                proyecto_view.crear()
                            case "3.2":
                                proyecto_view.listar()
                            case "3.3":
                                proyecto_view.buscar_por_id()
                            case "3.4":
                                proyecto_view.buscar_por_nombre()
                            case "3.5":
                                proyecto_view.modificar()
                            case "3.6":
                                proyecto_view.eliminar()
                            case "3.7":
                                proyecto_view.agregar_empleado()
                            case "3.8":
                                proyecto_view.quitar_empleado()
                            case "3.9":
                                proyecto_view.listar_empleados()
                            case "q":
                                break
                case "4":
                    registro_tiempo_view = RegistroTiempoView()
                    while True:
                        menu_registro_tiempo()
                        sub_opcion = input("Seleccione una opción: ")
                        match sub_opcion:
                            case "4.1":
                                registro_tiempo_view.crear()
                            case "4.2":
                                registro_tiempo_view.listar()
                            case "4.3":
                                registro_tiempo_view.buscar_por_id()
                            case "4.4":
                                registro_tiempo_view.modificar()
                            case "4.5":
                                registro_tiempo_view.buscar_por_id()
                            case "q":
                                break
                case "5":
                    exportar_view = ExportarView()
                    while True:
                        menu_exportar()
                        sub_opcion = input("Seleccione una opción: ")
                        match sub_opcion:
                            case "5.1":
                                exportar_view.exportar_excel()
                            case "5.2":
                                exportar_view.exportar_pdf()
                            case "q":
                                break
                case "6":
                    indicadoresView = IndicadoresView()
                    while True:
                        menu_indicadores_economicos()
                        sub_opcion = input("Seleccione una opción: ")
                        match sub_opcion:
                            case "6.1":
                                indicadoresView.consultar()
                            case "6.2":
                                pass
                            case "q":
                                break
                    pass
                case "q":
                    print("Saliendo del sistema...")
                    break


if __name__ == "__main__":
    main()
