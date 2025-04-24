# reportes.py
from fpdf import FPDF

def generar_pdf_mejores_marcas(marcas_por_evento):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Mejores Marcas por Prueba", ln=True, align="C")

    mejores = {}
    for evento in marcas_por_evento:
        for prueba in evento[1:]:
            cod_prueba = prueba[0]
            marcas = prueba[1:]
            for m in marcas:
                if cod_prueba not in mejores or mejor_que(m[2], mejores[cod_prueba][2]):
                    mejores[cod_prueba] = m

    for cod, marca in mejores.items():
        texto = f"Prueba: {cod} | Atleta: {marca[0]} | Dorsal: {marca[1]} | Marca: {marca[2]}"
        pdf.cell(200, 10, txt=texto, ln=True)

    pdf.output("reporte_mejores_marcas.pdf")

def generar_pdf_por_evento(marcas_por_evento, id_evento):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Marcas del Evento {id_evento}", ln=True, align="C")

    for evento in marcas_por_evento:
        if evento[0] == id_evento:
            for prueba in evento[1:]:
                pdf.cell(200, 10, txt=f"\nPrueba: {prueba[0]}", ln=True)
                for marca in prueba[1:]:
                    texto = f"Atleta: {marca[0]}, Dorsal: {marca[1]}, Marca: {marca[2]}"
                    pdf.cell(200, 10, txt=texto, ln=True)
            break

    pdf.output(f"reporte_evento_{id_evento}.pdf")

def generar_pdf_por_atleta(marcas_por_evento, id_atleta):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Marcas del Atleta {id_atleta}", ln=True, align="C")

    for evento in marcas_por_evento:
        id_evento = evento[0]
        for prueba in evento[1:]:
            for marca in prueba[1:]:
                if marca[0] == id_atleta:
                    texto = f"Evento: {id_evento}, Prueba: {prueba[0]}, Dorsal: {marca[1]}, Marca: {marca[2]}"
                    pdf.cell(200, 10, txt=texto, ln=True)

    pdf.output(f"reporte_atleta_{id_atleta}.pdf")

def mejor_que(marca1, marca2):
    try:
        return float(marca1) > float(marca2)
    except:
        return str(marca1) < str(marca2)