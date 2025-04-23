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
            print("[Consultar prueba - pendiente]")
        elif opcion == "3":
            print("[Modificar prueba - pendiente]")
        elif opcion == "4":
            print("[Eliminar prueba - pendiente]")
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
