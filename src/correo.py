# correo.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os

def enviar_reporte(destinatario, asunto, archivo_pdf, remitente, clave_app):
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto

    cuerpo = "Adjunto el reporte solicitado."
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    with open(archivo_pdf, 'rb') as f:
        parte = MIMEBase('application', 'octet-stream')
        parte.set_payload(f.read())
        encoders.encode_base64(parte)
        parte.add_header('Content-Disposition', f"attachment; filename={os.path.basename(archivo_pdf)}")
        mensaje.attach(parte)

    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(remitente, clave_app)
        servidor.send_message(mensaje)
        servidor.quit()
        print("Correo enviado correctamente a:", destinatario)
    except Exception as e:
        print("Error al enviar correo:", e)
