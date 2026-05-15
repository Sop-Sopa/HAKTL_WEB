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
        # Conectamos e imprimimos el rastro en la consola
        print("🔗 Intentando conectar con smtp.gmail.com...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.set_debuglevel(1)  # <<-- ESTO nos va a mostrar todo el diálogo con Google
        server.starttls()
        
        print("🔐 Intentando iniciar sesión...")
        server.login(remitente, password)
        
        print("🚀 Enviando correo...")
        server.sendmail(remitente, destinatario, msg.as_string())
        server.quit()
        print("✅ ¡Correo enviado con éxito!")
        return True
    except Exception as e:
        # Si falla, esto va a escupir el motivo exacto en la pantalla negra de Render
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