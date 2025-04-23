# pruebas.py

def menu_pruebas(pruebas, categorias, disciplinas, marcas_por_evento):
    while True:
        print("\nREGISTRAR PRUEBAS POR DISCIPLINA")
        print("1. Agregar prueba")
        print("2. Consultar prueba")
        print("3. Modificar prueba")
        print("4. Eliminar prueba")
        print("0. Volver al menú principal")

        opcion = input("OPCIÓN _ ")

        if opcion == "1":
            agregar_prueba(pruebas, categorias, disciplinas)
        elif opcion == "2":
            consultar_prueba(pruebas)
        elif opcion == "3":
            modificar_prueba(pruebas, categorias, disciplinas, marcas_por_evento)
        elif opcion == "4":
            eliminar_prueba(pruebas, marcas_por_evento)
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intente de nuevo.")

def agregar_prueba(pruebas, categorias, disciplinas):
    print("\nAGREGAR PRUEBA")
    while True:
        codigo = input("Código de la prueba (3 caracteres, letras/números): ").strip().upper()
        if codigo == "C":
            break
        if len(codigo) != 3 or not codigo.isalnum():
            print("Código inválido. Intente de nuevo.")
            continue
        if any(p[0] == codigo for p in pruebas):
            print("ESTA PRUEBA YA ESTÁ REGISTRADA, NO SE PUEDE AGREGAR")
            continue

        nombre = input("Nombre de la prueba (3 a 30 caracteres): ").strip()
        if not (3 <= len(nombre) <= 30):
            print("Nombre inválido.")
            continue

        categoria = input("Categoría (U12-U20, MAYOR, MASTER): ").strip().upper()
        if categoria not in categorias:
            print("Categoría inválida.")
            continue

        sexo = input("Sexo (F/M): ").strip().upper()
        if sexo not in ("F", "M"):
            print("Sexo inválido.")
            continue

        print("Disciplinas disponibles:")
        for d in disciplinas:
            print("-", d[0])
        disciplina = input("Nombre de la disciplina: ").strip()
        if disciplina not in [d[0] for d in disciplinas]:
            print("Disciplina no encontrada.")
            continue

        pruebas.append((codigo, nombre, categoria, sexo, disciplina))
        print("Prueba agregada con éxito.\n")
        break

def consultar_prueba(pruebas):
    print("\nCONSULTAR PRUEBA")
    codigo = input("Ingrese el código de la prueba: ").strip().upper()
    encontrada = False
    for prueba in pruebas:
        if prueba[0] == codigo:
            print(f"Código: {prueba[0]}")
            print(f"Nombre: {prueba[1]}")
            print(f"Categoría: {prueba[2]}")
            print(f"Sexo: {prueba[3]}")
            print(f"Disciplina: {prueba[4]}")
            encontrada = True
            break
    if not encontrada:
        print("No se encontró una prueba con ese código.")

def modificar_prueba(pruebas, categorias, disciplinas, marcas_por_evento):
    print("\nMODIFICAR PRUEBA")
    codigo = input("Ingrese el código de la prueba a modificar: ").strip().upper()

    prueba_existente = None
    for i, prueba in enumerate(pruebas):
        if prueba[0] == codigo:
            prueba_existente = (i, prueba)
            break

    if not prueba_existente:
        print("No se encontró una prueba con ese código.")
        return

    eventos = []
    for evento in marcas_por_evento:
        for p in evento[1:]:
            if p[0] == codigo:
                eventos.append(evento[0])

    if eventos:
        print("ESTA PRUEBA ESTÁ REGISTRADA EN UN EVENTO, NO SE PUEDE MODIFICAR")
        print("Eventos asociados:", eventos)
        return

    nombre = input("Nuevo nombre de la prueba (3 a 30 caracteres): ").strip()
    if not (3 <= len(nombre) <= 30):
        print("Nombre inválido.")
        return

    categoria = input("Nueva categoría (U12-U20, MAYOR, MASTER): ").strip().upper()
    if categoria not in categorias:
        print("Categoría inválida.")
        return

    sexo = input("Nuevo sexo (F/M): ").strip().upper()
    if sexo not in ("F", "M"):
        print("Sexo inválido.")
        return

    print("Disciplinas disponibles:")
    for d in disciplinas:
        print("-", d[0])
    disciplina = input("Nueva disciplina: ").strip()
    if disciplina not in [d[0] for d in disciplinas]:
        print("Disciplina no encontrada.")
        return

    pruebas[prueba_existente[0]] = (codigo, nombre, categoria, sexo, disciplina)
    print("Prueba modificada con éxito.")

def eliminar_prueba(pruebas, marcas_por_evento):
    print("\nELIMINAR PRUEBA")
    codigo = input("Ingrese el código de la prueba a eliminar: ").strip().upper()

    prueba_existente = None
    for i, prueba in enumerate(pruebas):
        if prueba[0] == codigo:
            prueba_existente = i
            break

    if prueba_existente is None:
        print("No se encontró una prueba con ese código.")
        return

    eventos = []
    for evento in marcas_por_evento:
        for p in evento[1:]:
            if p[0] == codigo:
                eventos.append(evento[0])

    if eventos:
        print("ESTA PRUEBA ESTÁ REGISTRADA EN UN EVENTO, NO SE PUEDE ELIMINAR")
        print("Eventos asociados:", eventos)
        return

    confirmacion = input("¿Está seguro que desea eliminar esta prueba? (S/N): ").strip().upper()
    if confirmacion == "S":
        del pruebas[prueba_existente]
        print("Prueba eliminada con éxito.")
    else:
        print("Eliminación cancelada.")
