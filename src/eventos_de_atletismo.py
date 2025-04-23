# eventos_de_atletismo.py

import re
from datetime import datetime

# ----------------------------
# Estructuras de datos globales
# ----------------------------
disciplinas = [
    ("Carreras de fondo", "T"),
    ("Carreras de medio fondo", "T"),
    ("Carreras de obstáculos", "T"),
    ("Carreras de relevos", "T"),
    ("Carreras de velocidad", "T"),
    ("Lanzamientos", "M"),
    ("Saltos", "M"),
    ("Marcha", "T")
]

categorias = ("U12", "U13", "U14", "U15", "U16", "U17", "U18", "U20", "MAYOR", "MASTER")
pruebas = []
atletas = []
eventos = []
marcas_por_evento = []

# ----------------------------
# Utilidades y validaciones
# ----------------------------
def formato_valido_correo(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(patron, correo) is not None

def dominio_valido(correo):
    dominios_validos = ["gmail.com", "yahoo.com", "outlook.com", "tec.ac.cr"]
    try:
        dominio = correo.split('@')[1]
        return dominio in dominios_validos
    except:
        return False

def prueba_en_eventos(codigo_prueba):
    eventos_con_prueba = []
    for evento in marcas_por_evento:
        id_evento = evento[0]
        pruebas_evento = evento[1:]
        for prueba in pruebas_evento:
            if prueba[0] == codigo_prueba:
                eventos_con_prueba.append(id_evento)
    return eventos_con_prueba

# ----------------------------
# Menú principal
# ----------------------------
def menu_principal():
    while True:
        print("\nEVENTOS DE ATLETISMO")
        print("1. Lista de disciplinas")
        print("2. Registrar pruebas por disciplina")
        print("3. Registrar atletas")
        print("4. Registrar eventos")
        print("5. Registrar marcas")
        print("6. Análisis de datos")
        print("7. Ayuda")
        print("8. Acerca de")
        print("0. Salir")

        opcion = input("OPCIÓN _ ")

        if opcion == "1":
            listar_disciplinas()
        elif opcion == "2":
            menu_pruebas()
        elif opcion == "3":
            menu_atletas()
        elif opcion == "4":
            menu_eventos()
        elif opcion == "5":
            menu_marcas()
        elif opcion == "6":
            menu_analisis()
        elif opcion == "7":
            mostrar_ayuda()
        elif opcion == "8":
            mostrar_acerca_de()
        elif opcion == "0":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("\nOpción inválida. Intente de nuevo.")

# ----------------------------
# Funcionalidades
# ----------------------------
def listar_disciplinas():
    print("\nLISTA DE DISCIPLINAS")
    print(f"{'NOMBRE DE LA DISCIPLINA':<30} {'MEDIDA'}")
    for nombre, medida in disciplinas:
        medida_texto = "Tiempo" if medida == "T" else "Metros"
        print(f"{nombre:<30} {medida_texto}")
    input("\nPresione ENTER para continuar...")

def menu_pruebas():
    while True:
        print("\nREGISTRAR PRUEBAS POR DISCIPLINA")
        print("1. Agregar prueba")
        print("2. Consultar prueba")
        print("3. Modificar prueba")
        print("4. Eliminar prueba")
        print("0. Volver al menú principal")

        opcion = input("OPCIÓN _ ")

        if opcion == "1":
            agregar_prueba()
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

def agregar_prueba():
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

def menu_atletas():
    print("\n[Submenú: Registrar atletas]")
    # Aquí se desarrollará el CRUD de atletas

def menu_eventos():
    print("\n[Submenú: Registrar eventos]")
    # Aquí se desarrollará el CRUD de eventos

def menu_marcas():
    print("\n[Submenú: Registrar marcas]")
    # Aquí se desarrollará el CRUD de marcas

def menu_analisis():
    print("\n[Submenú: Análisis de datos]")
    # Aquí se desarrollará el análisis y generación de reportes en PDF

def mostrar_ayuda():
    print("\n[Manual de usuario en PDF desplegado aquí]")
    # Simulación de mostrar ayuda

def mostrar_acerca_de():
    print("\nPrograma: Eventos de Atletismo\nVersión: 1.0\nAutor: Tu Nombre\nFecha: Abril 2025")

# ----------------------------
# Ejecución
# ----------------------------
if __name__ == "__main__":
    menu_principal()