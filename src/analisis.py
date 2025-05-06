# --------------------------------------------------
# MÓDULO: ANÁLISIS DE DATOS Y REPORTES
# Autor: Santiago Villarreal Arley
# Carné: 2025120897
# Fecha: 4 de mayo 2025
# --------------------------------------------------

from reportes import generar_pdf_mejores_marcas, generar_pdf_por_evento, generar_pdf_por_atleta
from correo import enviar_reporte

def menu_analisis(marcas_por_evento):
    """
    Despliega el menú de análisis de datos con múltiples opciones:
    - Visualizar mejores marcas
    - Generar y enviar reportes PDF por atleta o evento

    Entradas:
    - marcas_por_evento (list): estructura de eventos, pruebas y marcas.

    Salidas:
    - Muestra información en consola y puede generar/enviar archivos PDF.
    """
    while True:
        print("\nANÁLISIS DE DATOS")
        print("1. Marcas por evento")
        print("2. Marcas por atleta")
        print("3. Mejores marcas por prueba")
        print("4. Generar PDF de mejores marcas")
        print("5. Generar PDF por evento")
        print("6. Generar PDF por atleta")
        print("7. Enviar reporte PDF por correo")
        print("0. Volver al menú principal")

        opcion = input("OPCIÓN _ ")

        if opcion == "1":
            marcas_ordenadas_por_evento(marcas_por_evento)

        elif opcion == "2":
            id_atleta = input("Ingrese el ID del atleta (o ENTER para todos): ").strip()
            enviar_correos = input("¿Desea enviar reportes a los atletas encontrados? (S/N): ").strip().upper()
            remitente = clave = None
            if enviar_correos == "S":
                remitente = input("Correo remitente (Gmail): ").strip()
                clave = input("Contraseña de aplicación del remitente: ").strip()

            atletas_filtrados = set()
            for evento in marcas_por_evento:
                for prueba in evento[1:]:
                    for marca in prueba[1:]:
                        if not id_atleta or marca[0] == id_atleta:
                            atletas_filtrados.add(marca[0])

            for atleta_id in sorted(atletas_filtrados):
                generar_pdf_por_atleta(marcas_por_evento, atleta_id)
                print(f"PDF generado: reporte_atleta_{atleta_id}.pdf")
                if enviar_correos == "S":
                    destinatario = input(f"Correo para atleta {atleta_id}: ").strip()
                    asunto = f"Reporte de participación - {atleta_id}"
                    archivo = f"reporte_atleta_{atleta_id}.pdf"
                    enviar_reporte(destinatario, asunto, archivo, remitente, clave)

        elif opcion == "3":
            mejores_marcas_por_prueba(marcas_por_evento)

        elif opcion == "4":
            generar_pdf_mejores_marcas(marcas_por_evento)
            print("PDF generado: reporte_mejores_marcas.pdf")

        elif opcion == "5":
            try:
                id_evento = input("Ingrese el ID del evento (o ENTER para todos): ").strip()
                if id_evento:
                    generar_pdf_por_evento(marcas_por_evento, int(id_evento))
                    print(f"PDF generado: reporte_evento_{id_evento}.pdf")
                else:
                    for evento in marcas_por_evento:
                        generar_pdf_por_evento(marcas_por_evento, evento[0])
                    print("PDFs generados para todos los eventos.")
            except:
                print("ID inválido.")

        elif opcion == "6":
            id_atleta = input("Ingrese el ID del atleta (o ENTER para todos): ").strip()
            if id_atleta:
                generar_pdf_por_atleta(marcas_por_evento, id_atleta)
                print(f"PDF generado: reporte_atleta_{id_atleta}.pdf")
            else:
                atletas_ids = set(m[0] for e in marcas_por_evento for p in e[1:] for m in p[1:])
                for atleta_id in atletas_ids:
                    generar_pdf_por_atleta(marcas_por_evento, atleta_id)
                print("PDFs generados para todos los atletas.")

        elif opcion == "7":
            destinatario = input("Correo destinatario: ").strip()
            archivo = input("Nombre del archivo PDF (ej: reporte_mejores_marcas.pdf): ").strip()
            remitente = input("Correo remitente (Gmail): ").strip()
            clave = input("Contraseña de aplicación del remitente: ").strip()
            asunto = input("Asunto del correo: ").strip()
            enviar_reporte(destinatario, asunto, archivo, remitente, clave)

        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intente de nuevo.")

def mejores_marcas_por_prueba(marcas_por_evento):
    """
    Muestra en consola la mejor marca registrada por cada prueba.

    Entradas:
    - marcas_por_evento (list): estructura anidada de eventos y marcas.

    Salidas:
    - Imprime los datos en pantalla.
    """
    print("\nMEJORES MARCAS POR PRUEBA")
    mejores = {}
    for evento in marcas_por_evento:
        for prueba in evento[1:]:
            cod_prueba = prueba[0]
            marcas = prueba[1:]
            for m in marcas:
                if cod_prueba not in mejores or mejor_que(m[2], mejores[cod_prueba][2]):
                    mejores[cod_prueba] = m

    for cod, marca in mejores.items():
        print(f"Prueba: {cod} | Atleta: {marca[0]} | Dorsal: {marca[1]} | Marca: {marca[2]}")

def marcas_ordenadas_por_evento(marcas_por_evento):
    """
    Muestra todas las marcas agrupadas por evento y ordenadas por marca.

    Entradas:
    - marcas_por_evento (list): estructura de marcas por evento y prueba.

    Salidas:
    - Información impresa por consola.
    """
    print("\nMARCAS POR EVENTO")
    for evento in marcas_por_evento:
        print(f"\nEvento ID: {evento[0]}")
        for prueba in evento[1:]:
            cod_prueba = prueba[0]
            marcas = sorted(prueba[1:], key=lambda x: x[2])  # Simplificada
            print(f"Prueba: {cod_prueba}")
            for m in marcas:
                print(f"Atleta: {m[0]}, Dorsal: {m[1]}, Marca: {m[2]}")

def mejor_que(marca1, marca2):
    """
    Compara dos marcas para decidir cuál es mejor.

    Entradas:
    - marca1 (str)
    - marca2 (str)

    Salidas:
    - True si marca1 es mejor, False si no lo es.
    """
    try:
        return float(marca1) > float(marca2)
    except:
        return str(marca1) < str(marca2)
