# --------------------------------------------------
# MÓDULO: GESTIÓN DE MARCAS - EVENTOS DE ATLETISMO
# Autor: Santiago Villarreal Arley
# Carné: 2025120897
# Fecha: 1 de mayo 2025
# --------------------------------------------------

def menu_marcas(marcas_por_evento, pruebas, atletas, eventos):
    """
    Despliega el menú de gestión de marcas y redirige a las opciones correspondientes.

    Entradas:
    - marcas_por_evento (list): lista anidada de marcas agrupadas por evento y prueba.
    - pruebas (list): lista de pruebas registradas.
    - atletas (list): lista de atletas.
    - eventos (list): lista de eventos.

    Salidas:
    - Interacción de usuario por consola.
    """
    while True:
        print("\nREGISTRAR MARCAS")
        print("1. Agregar marca")
        print("2. Consultar marcas por evento")
        print("3. Consultar marcas por atleta")
        print("0. Volver al menú principal")

        opcion = input("OPCIÓN _ ")

        if opcion == "1":
            agregar_marca(marcas_por_evento, pruebas, atletas, eventos)
        elif opcion == "2":
            consultar_marcas_por_evento(marcas_por_evento, eventos)
        elif opcion == "3":
            consultar_marcas_por_atleta(marcas_por_evento, atletas)
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intente de nuevo.")

def agregar_marca(marcas_por_evento, pruebas, atletas, eventos):
    """
    Registra una nueva marca para un atleta en una prueba específica de un evento.

    Entradas:
    - marcas_por_evento (list): lista anidada que contiene marcas organizadas por evento.
    - pruebas (list): lista de pruebas.
    - atletas (list): lista de atletas.
    - eventos (list): lista de eventos.

    Salidas:
    - Modifica la estructura de marcas_por_evento si la marca es válida.
    """
    print("\nAGREGAR MARCA")
    try:
        id_evento = int(input("ID del evento: "))
    except ValueError:
        print("ID inválido.")
        return

    if not any(e[0] == id_evento for e in eventos):
        print("Evento no encontrado.")
        return

    codigo_prueba = input("Código de la prueba: ").strip().upper()
    if not any(p[0] == codigo_prueba for p in pruebas):
        print("Prueba no encontrada.")
        return

    id_atleta = input("ID del atleta: ").strip()
    if not any(a[0] == id_atleta for a in atletas):
        print("Atleta no encontrado.")
        return

    try:
        dorsal = int(input("Dorsal asignado (número entero): "))
    except ValueError:
        print("Dorsal inválido.")
        return

    marca = input("Marca (formato según tipo de prueba): ").strip()

    evento = next((e for e in marcas_por_evento if e[0] == id_evento), None)
    if evento:
        for p in evento[1:]:
            if p[0] == codigo_prueba:
                p.append((id_atleta, dorsal, marca))
                print("Marca agregada correctamente.")
                return
        evento.append([codigo_prueba, (id_atleta, dorsal, marca)])
    else:
        marcas_por_evento.append([id_evento, [codigo_prueba, (id_atleta, dorsal, marca)]])

    print("Marca agregada correctamente.")

def consultar_marcas_por_evento(marcas_por_evento, eventos):
    """
    Muestra todas las marcas registradas en un evento específico.

    Entradas:
    - marcas_por_evento (list): lista de marcas.
    - eventos (list): lista de eventos disponibles.

    Salidas:
    - Muestra marcas organizadas por prueba en consola.
    """
    print("\nCONSULTAR MARCAS POR EVENTO")
    try:
        id_evento = int(input("ID del evento: "))
    except ValueError:
        print("ID inválido.")
        return

    for evento in marcas_por_evento:
        if evento[0] == id_evento:
            print(f"\nMarcas registradas para el evento {id_evento}:")
            for prueba in evento[1:]:
                print(f"\nPrueba: {prueba[0]}")
                for registro in prueba[1:]:
                    print(f"Atleta: {registro[0]}, Dorsal: {registro[1]}, Marca: {registro[2]}")
            return

    print("No hay marcas registradas para ese evento.")

def consultar_marcas_por_atleta(marcas_por_evento, atletas):
    """
    Muestra todas las marcas asociadas a un atleta específico.

    Entradas:
    - marcas_por_evento (list): lista de marcas.
    - atletas (list): lista de atletas.

    Salidas:
    - Imprime todas las marcas del atleta si existen.
    """
    print("\nCONSULTAR MARCAS POR ATLETA")
    id_atleta = input("ID del atleta: ").strip()

    existe = any(a[0] == id_atleta for a in atletas)
    if not existe:
        print("Atleta no encontrado.")
        return

    encontrado = False
    for evento in marcas_por_evento:
        id_evento = evento[0]
        for prueba in evento[1:]:
            codigo_prueba = prueba[0]
            for marca in prueba[1:]:
                if marca[0] == id_atleta:
                    if not encontrado:
                        print(f"\nMarcas registradas para el atleta {id_atleta}:")
                        encontrado = True
                    print(f"Evento: {id_evento}, Prueba: {codigo_prueba}, Dorsal: {marca[1]}, Marca: {marca[2]}")

    if not encontrado:
        print("No hay marcas registradas para ese atleta.")
