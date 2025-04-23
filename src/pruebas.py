# atletas.py
import re
from datetime import datetime

def menu_atletas(atletas):
    while True:
        print("\nREGISTRAR ATLETAS")
        print("1. Agregar atleta")
        print("2. Consultar atleta")
        print("3. Modificar atleta")
        print("4. Eliminar atleta")
        print("0. Volver al menú principal")

        opcion = input("OPCIÓN _ ")

        if opcion == "1":
            agregar_atleta(atletas)
        elif opcion == "2":
            consultar_atleta(atletas)
        elif opcion == "3":
            modificar_atleta(atletas)
        elif opcion == "4":
            eliminar_atleta(atletas)
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intente de nuevo.")

def agregar_atleta(atletas):
    print("\nAGREGAR ATLETA")

    identificacion = input("Identificación (única, 9-20 caracteres): ").strip()
    if not (9 <= len(identificacion) <= 20):
        print("Identificación inválida.")
        return
    if any(a[0] == identificacion for a in atletas):
        print("YA EXISTE UN ATLETA CON ESA IDENTIFICACIÓN")
        return

    nombre = input("Nombre (2-20 caracteres): ").strip()
    if not (2 <= len(nombre) <= 20):
        print("Nombre inválido.")
        return

    apellido = input("Apellido (2-20 caracteres): ").strip()
    if not (2 <= len(apellido) <= 20):
        print("Apellido inválido.")
        return

    sexo = input("Sexo (F/M): ").strip().upper()
    if sexo not in ("F", "M"):
        print("Sexo inválido.")
        return

    pais = input("País (código ISO alfa-3): ").strip().upper()
    if len(pais) != 3:
        print("Código de país inválido.")
        return

    fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    except ValueError:
        print("Formato de fecha inválido.")
        return

    correo = input("Correo electrónico: ").strip()
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$', correo):
        print("Formato de correo inválido.")
        return
    dominio = correo.split("@")[1]
    if dominio not in ["gmail.com", "yahoo.com", "outlook.com", "tec.ac.cr"]:
        print("Dominio de correo no permitido.")
        return

    telefono = input("Teléfono (8-25 caracteres): ").strip()
    if not (8 <= len(telefono) <= 25):
        print("Teléfono inválido.")
        return

    atletas.append((identificacion, nombre, apellido, sexo, pais, fecha_nacimiento, correo, telefono))
    print("Atleta registrado con éxito.")

def consultar_atleta(atletas):
    print("\nCONSULTAR ATLETA")
    identificacion = input("Ingrese la identificación del atleta: ").strip()
    encontrado = False
    for atleta in atletas:
        if atleta[0] == identificacion:
            print(f"Identificación: {atleta[0]}")
            print(f"Nombre: {atleta[1]} {atleta[2]}")
            print(f"Sexo: {atleta[3]}")
            print(f"País: {atleta[4]}")
            print(f"Fecha de nacimiento: {atleta[5]}")
            print(f"Correo electrónico: {atleta[6]}")
            print(f"Teléfono: {atleta[7]}")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró un atleta con esa identificación.")

def modificar_atleta(atletas):
    print("\nMODIFICAR ATLETA")
    identificacion = input("Ingrese la identificación del atleta a modificar: ").strip()

    indice = None
    for i, atleta in enumerate(atletas):
        if atleta[0] == identificacion:
            indice = i
            break

    if indice is None:
        print("No se encontró un atleta con esa identificación.")
        return

    nombre = input("Nuevo nombre (2-20 caracteres): ").strip()
    if not (2 <= len(nombre) <= 20):
        print("Nombre inválido.")
        return

    apellido = input("Nuevo apellido (2-20 caracteres): ").strip()
    if not (2 <= len(apellido) <= 20):
        print("Apellido inválido.")
        return

    sexo = input("Nuevo sexo (F/M): ").strip().upper()
    if sexo not in ("F", "M"):
        print("Sexo inválido.")
        return

    pais = input("Nuevo país (ISO alfa-3): ").strip().upper()
    if len(pais) != 3:
        print("Código de país inválido.")
        return

    fecha_nacimiento = input("Nueva fecha de nacimiento (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    except ValueError:
        print("Formato de fecha inválido.")
        return

    correo = input("Nuevo correo electrónico: ").strip()
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$', correo):
        print("Formato de correo inválido.")
        return
    dominio = correo.split("@")[1]
    if dominio not in ["gmail.com", "yahoo.com", "outlook.com", "tec.ac.cr"]:
        print("Dominio de correo no permitido.")
        return

    telefono = input("Nuevo teléfono (8-25 caracteres): ").strip()
    if not (8 <= len(telefono) <= 25):
        print("Teléfono inválido.")
        return

    atletas[indice] = (identificacion, nombre, apellido, sexo, pais, fecha_nacimiento, correo, telefono)
    print("Atleta modificado con éxito.")

def eliminar_atleta(atletas):
    print("\nELIMINAR ATLETA")
    identificacion = input("Ingrese la identificación del atleta a eliminar: ").strip()

    for i, atleta in enumerate(atletas):
        if atleta[0] == identificacion:
            confirmar = input(f"¿Está seguro que desea eliminar al atleta {atleta[1]} {atleta[2]}? (S/N): ").strip().upper()
            if confirmar == "S":
                del atletas[i]
                print("Atleta eliminado con éxito.")
            else:
                print("Eliminación cancelada.")
            return

    print("No se encontró un atleta con esa identificación.")
