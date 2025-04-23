# eventos_de_atletismo.py

import re
from datetime import datetime
from pruebas import menu_pruebas  # Importamos el menú de pruebas desde módulo externo
from eventos import menu_eventos  # Importamos el menú de eventos desde módulo externo
from atletas import menu_atletas  # Importamos el menú de atletas desde módulo externo
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
            menu_pruebas(pruebas, categorias, disciplinas, marcas_por_evento)
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
    print("\nPrograma: Eventos de Atletismo\nVersión: 1.0\nAutor: Santiago Villarreal Arley\nFecha: Abril 2025")

# ----------------------------
# Ejecución
# ----------------------------
if __name__ == "__main__":
    menu_principal()
