from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# RUTA PRINCIPAL: Muestra la página y procesa el formulario
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Capturamos los datos que el usuario escribió en el HTML
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        mensaje = request.form.get('mensaje')
        
        # Por ahora, imprimimos los datos en la terminal del servidor para verificar
        print("\n" + "="*40)
        print("📥 ¡NUEVA CONSULTA RECIBIDA EN HAKTL!")
        print(f"Nombre:  {nombre}")
        print(f"Email:   {email}")
        print(f"Mensaje: {mensaje}")
        print("="*40 + "\n")
        
        # Redirige a la misma página limpia para evitar envíos duplicados al recargar
        return redirect(url_for('home'))
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)