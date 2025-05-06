# --------------------------------------------------
# MÓDULO: GESTIÓN DE EVENTOS - EVENTOS DE ATLETISMO
# Autor: Santiago Villarreal Arley
# Carné: 2025120897
# Fecha: 2 de mayo 2025
# --------------------------------------------------

from datetime import datetime

def menu_eventos(eventos):
    """
    Muestra el menú principal de gestión de eventos y redirige a cada acción.

    Entradas:
    - eventos (list): lista de eventos existentes.

    Salidas:
    - Ejecuta interacciones de usuario por consola.
    """
    while True:
        print("\nREGISTRAR EVENTOS")
        print("1. Agregar evento")
        print("2. Consultar evento")
        print("3. Modificar evento")
        print("4. Eliminar evento")
        print("0. Volver al menú principal")

        opcion = input("OPCIÓN _ ")

        if opcion == "1":
            agregar_evento(eventos)
        elif opcion == "2":
            consultar_evento(eventos)
        elif opcion == "3":
            modificar_evento(eventos)
        elif opcion == "4":
            eliminar_evento(eventos)
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intente de nuevo.")

def agregar_evento(eventos):
    """
    Permite agregar un nuevo evento validando sus atributos.

    Entradas:
    - eventos (list): lista de eventos donde se añadirá el nuevo evento.

    Salidas:
    - Agrega una nueva tupla de evento si los datos son válidos.
    """
    print("\nAGREGAR EVENTO")

    try:
        id_evento = int(input("ID del evento (entero único): "))
    except ValueError:
        print("ID inválido. Debe ser un número entero.")
        return

    if any(e[0] == id_evento for e in eventos):
        print("YA EXISTE UN EVENTO CON ESE ID")
        return

    nombre = input("Nombre del evento (5-60 caracteres): ").strip()
    if not (5 <= len(nombre) <= 60):
        print("Nombre inválido.")
        return

    pais = input("País anfitrión (ISO alfa-3): ").strip().upper()
    if len(pais) != 3:
        print("Código de país inválido.")
        return

    lugar = input("Lugar (5-60 caracteres): ").strip()
    if not (5 <= len(lugar) <= 60):
        print("Lugar inválido.")
        return

    fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ").strip()
    fecha_fin = input("Fecha de fin (YYYY-MM-DD): ").strip()
    try:
        inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
        if inicio > fin:
            print("La fecha de inicio no puede ser posterior a la fecha de fin.")
            return
    except ValueError:
        print("Formato de fecha inválido.")
        return

    eventos.append((id_evento, nombre, pais, lugar, fecha_inicio, fecha_fin))
    print("Evento registrado con éxito.")

def consultar_evento(eventos):
    """
    Muestra los detalles de un evento según su ID.

    Entradas:
    - eventos (list): lista de eventos.

    Salidas:
    - Imprime por consola la información del evento, si existe.
    """
    print("\nCONSULTAR EVENTO")
    try:
        id_evento = int(input("Ingrese el ID del evento: "))
    except ValueError:
        print("ID inválido.")
        return

    for evento in eventos:
        if evento[0] == id_evento:
            print(f"ID: {evento[0]}")
            print(f"Nombre: {evento[1]}")
            print(f"País: {evento[2]}")
            print(f"Lugar: {evento[3]}")
            print(f"Fecha de inicio: {evento[4]}")
            print(f"Fecha de fin: {evento[5]}")
            return

    print("No se encontró un evento con ese ID.")

def modificar_evento(eventos):
    """
    Permite modificar todos los atributos de un evento dado su ID.

    Entradas:
    - eventos (list): lista de eventos.

    Salidas:
    - Actualiza la tupla del evento si el ID es válido.
    """
    print("\nMODIFICAR EVENTO")
    try:
        id_evento = int(input("Ingrese el ID del evento a modificar: "))
    except ValueError:
        print("ID inválido.")
        return

    for i, evento in enumerate(eventos):
        if evento[0] == id_evento:
            nombre = input("Nuevo nombre del evento (5-60 caracteres): ").strip()
            if not (5 <= len(nombre) <= 60):
                print("Nombre inválido.")
                return

            pais = input("Nuevo país anfitrión (ISO alfa-3): ").strip().upper()
            if len(pais) != 3:
                print("Código de país inválido.")
                return

            lugar = input("Nuevo lugar (5-60 caracteres): ").strip()
            if not (5 <= len(lugar) <= 60):
                print("Lugar inválido.")
                return

            fecha_inicio = input("Nueva fecha de inicio (YYYY-MM-DD): ").strip()
            fecha_fin = input("Nueva fecha de fin (YYYY-MM-DD): ").strip()
            try:
                inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
                fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
                if inicio > fin:
                    print("La fecha de inicio no puede ser posterior a la fecha de fin.")
                    return
            except ValueError:
                print("Formato de fecha inválido.")
                return

            eventos[i] = (id_evento, nombre, pais, lugar, fecha_inicio, fecha_fin)
            print("Evento modificado con éxito.")
            return

    print("No se encontró un evento con ese ID.")

def eliminar_evento(eventos):
    """
    Permite eliminar un evento del sistema, solicitando confirmación previa.

    Entradas:
    - eventos (list): lista de eventos.

    Salidas:
    - Elimina el evento si se confirma la acción.
    """
    print("\nELIMINAR EVENTO")
    try:
        id_evento = int(input("Ingrese el ID del evento a eliminar: "))
    except ValueError:
        print("ID inválido.")
        return

    for i, evento in enumerate(eventos):
        if evento[0] == id_evento:
            confirmar = input(f"¿Está seguro que desea eliminar el evento '{evento[1]}'? (S/N): ").strip().upper()
            if confirmar == "S":
                del eventos[i]
                print("Evento eliminado con éxito.")
            else:
                print("Eliminación cancelada.")
            return

    print("No se encontró un evento con ese ID.")
