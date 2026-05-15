import os
import smtplib
from email.mime.text import MIMEText
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def enviar_correo(nombre, email_cliente, mensaje_cliente):
    remitente = os.environ.get('EMAIL_USER')
    password = os.environ.get('EMAIL_PASS')
    destinatario = "haktl.digital@gmail.com"

    if not remitente or not password:
        print("⚠️ Variables de entorno ausentes en el servidor.")
        return False

    asunto = f"📥 Nueva consulta web de {nombre}"
    cuerpo = f"""
    Has recibido un nuevo mensaje desde el formulario de HAKTL:
    
    Nombre: {nombre}
    Email:  {email_cliente}
    
    Mensaje:
    {mensaje_cliente}
    """
    
    msg = MIMEText(cuerpo)
    msg['Subject'] = asunto
    msg['From'] = remitente
    msg['To'] = destinatario

    try:
        print("🔗 Intentando conectar con smtp.gmail.com usando puerto 465 (SSL)...")
        # Cambiamos a SMTP_SSL y puerto 465 para saltear el bloqueo de Render
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.set_debuglevel(1)
        
        print("🔐 Intentando iniciar sesión...")
        server.login(remitente, password)
        
        print("🚀 Enviando correo...")
        server.sendmail(remitente, destinatario, msg.as_string())
        server.quit()
        print("✅ ¡Correo enviado con éxito!")
        return True
    except Exception as e:
        print(f"❌ ERROR CRÍTICO AL ENVIAR: {e}")
        return False

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        mensaje = request.form.get('mensaje')
        
        print(f"\nProcesando envío para: {nombre}")
        enviar_correo(nombre, email, mensaje)
        
        return redirect(url_for('home'))
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)