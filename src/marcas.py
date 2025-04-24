# marcas.py

def menu_marcas(marcas_por_evento, pruebas, atletas, eventos):
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

    # Buscar evento existente en la lista
    evento = next((e for e in marcas_por_evento if e[0] == id_evento), None)
    if evento:
        # Buscar prueba dentro del evento
        for p in evento[1:]:
            if p[0] == codigo_prueba:
                p.append((id_atleta, dorsal, marca))
                print("Marca agregada correctamente.")
                return
        # Si la prueba no está en el evento, se agrega con la marca
        evento.append([codigo_prueba, (id_atleta, dorsal, marca)])
    else:
        marcas_por_evento.append([id_evento, [codigo_prueba, (id_atleta, dorsal, marca)]])

    print("Marca agregada correctamente.")

def consultar_marcas_por_evento(marcas_por_evento, eventos):
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
