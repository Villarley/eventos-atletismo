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
            print("[Consultar atleta - pendiente]")
        elif opcion == "3":
            print("[Modificar atleta - pendiente]")
        elif opcion == "4":
            print("[Eliminar atleta - pendiente]")
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