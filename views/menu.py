# views/menu.py

def menu_inicio():
    print("--- Inicio de sesión ---")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("q. Salir")


def menu_principal():
    print("--- Menu Principal ---")
    print("1. Registro de Empleados")
    print("2. Gestión de Departamentos")
    print("3. Gestion de Proyectos")
    print("4. Gestion de Registro de Tiempo")
    print("5. Exportar")
    print("6. Indicadores Económicos")
    print("q. Salir")


def menu_empleado():
    print("--- Gestión Empleados ---")
    print("1.1 Crear Empleado")
    print("1.2 Listar Empleado")
    print("1.3 Buscar Empleado por RUT")
    print("1.4 Buscar Empleado por ID")
    print("1.5 Modificar Empleado")
    print("1.6 Eliminar Empleado")
    print("q. Volver al menu Principal")


def menu_departamento():
    print("--- Gestión Departamentos ---")
    print("2.1 Crear Departamento")
    print("2.2 Listar Departamentos")
    print("2.3 Buscar Departamento por id")
    print("2.4 Buscar Departamento por nombre")
    print("2.5 Modificar Departamento")
    print("2.6 Eliminar Departamento")
    print("q. Volver al menu Principal")


def menu_proyecto():
    print("--- Gestión Proyectos ---")
    print("3.1 Crear Proyecto")
    print("3.2 Listar Proyectos")
    print("3.3 Buscar Proyecto por id")
    print("3.4 Buscar Proyecto por nombre")
    print("3.5 Modificar Proyecto")
    print("3.6 Eliminar Proyecto")
    print("3.7 Agregar Empleado a Proyecto")
    print("3.8 Remover Empleado de Proyecto")
    print("3.9 Listar empleados de un Proyecto")
    print("q. Volver al menu Principal")


def menu_registro_tiempo():
    print("--- Gestión Registros Tiempo ---")
    print("4.1 Crear Registro de Tiempo")
    print("4.2 Listar Registros de Tiempo")
    print("4.3 Buscar Registro de Tiempo por id")
    print("4.4 Modificar Registro de Tiempo")
    print("4.5 Eliminar Registro de Tiempo")
    print("q. Volver al menu Principal")


def menu_exportar():
    print("--- Gestión Exportar ---")
    print("5.1 Exportar Excel")
    print("5.2 Exportar PDF")
    print("q. Volver al menu principal")


def menu_indicadores_economicos():
    print("--- Indicadores Económicos ---")
    print("6.1 Consultar Indicadores Económicos")
    print("6.2 Registrar Indicadores Económicos")
    print("q. Volver al menu principal")


def menu_indicadores():
    print("1. Unidad de Fomento (UF)")
    print("2. Índice de valor Promedio (IVP)")
    print("3. Índice de Precio al Consumidor (IPC)")
    print("4. Unidad Tributaria Mensual (UTM)")
    print("5. Dólar Observado")
    print("6. Euro")
    print("q. Salir")
