# eventos_de_atletismo.py

import re
import os
import platform
from datetime import datetime
from pruebas import menu_pruebas  # Importamos el menú de pruebas desde módulo externo
from eventos import menu_eventos  # Importamos el menú de eventos desde módulo externo
from atletas import menu_atletas  # Importamos el menú de atletas desde módulo externo
from marcas import menu_marcas  # Importamos el menú de marcas desde módulo externo
from analisis import menu_analisis  # Importamos el menú de análisis desde módulo externo
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

pruebas = [
    ("V01", "100m planos", "U18", "M", "Carreras de velocidad"),
    ("S02", "Salto largo", "MAYOR", "F", "Saltos")
]

atletas = [
    ("A001", "Juan", "Pérez", "M", "CRC", "2007-06-01", "villarley.softdev@gmail.com", "88888888"),
    ("A002", "María", "Soto", "F", "CRC", "1999-03-15", "jsebascp04@gmail.com", "87777777"),
    ("A003", "Carlos", "Ramírez", "M", "CRC", "2001-01-10", "santivillarley1010@gmail.com", "83334444"),
    ("A004", "Lucía", "Gómez", "F", "CRC", "2003-11-23", "s.villarreal.1@estudiantec.cr", "81112222")
]

eventos = [
    (101, "Nacionales Juveniles", "CRC", "San José", "2025-05-01", "2025-05-05"),
    (102, "Open Atletismo", "CRC", "Cartago", "2025-04-20", "2025-04-22")
]

marcas_por_evento = [
    [101,
        ["V01", ("A001", 1, "11.23"), ("A003", 2, "11.45")],
        ["S02", ("A002", 4, "5.42"), ("A004", 5, "5.12")]
    ],
    [102,
        ["V01", ("A001", 6, "11.10"), ("A003", 7, "11.50")]
    ]
]

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
            menu_pruebas(pruebas, categorias, disciplinas, marcas_por_evento)
        elif opcion == "3":
            menu_atletas(atletas)
        elif opcion == "4":
            menu_eventos(eventos)
        elif opcion == "5":
            menu_marcas(marcas_por_evento, pruebas, atletas, eventos)
        elif opcion == "6":
            menu_analisis(marcas_por_evento)
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

def mostrar_ayuda():
    print("\nAbriendo manual de usuario...")
    ruta_manual = "../docs/manual_usuario.pdf"

    if os.path.exists(ruta_manual):
        if platform.system() == "Windows":
            os.startfile(ruta_manual)
        elif platform.system() == "Darwin":  # macOS
            os.system(f"open '{ruta_manual}'")
        else:  # Linux y otros
            os.system(f"xdg-open '{ruta_manual}'")
    else:
        print("No se encontró el archivo del manual en docs/manual_usuario.pdf")

def mostrar_acerca_de():
    print("\nPrograma: Eventos de Atletismo\nVersión: 1.0\nAutor: Santiago Villarreal Arley\nFecha: Abril 2025")

# ----------------------------
# Ejecución
# ----------------------------
if __name__ == "__main__":
    menu_principal()
