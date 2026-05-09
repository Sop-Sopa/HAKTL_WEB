from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <body style="background-color: #0b0b0b; color: #d1d1d1; font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0;">
        <div style="text-align: center; border: 1px solid #333; padding: 40px; border-radius: 10px; background-color: #121212;">
            <h1 style="color: #ffffff; letter-spacing: 5px;">HAKTL</h1>
            <p style="color: #888;">INGENIERÍA DIGITAL | SAN JUAN</p>
            <hr style="border: 0; border-top: 1px solid #333; margin: 20px 0;">
            <p>Web en desarrollo - Próximamente soluciones en Python</p>
        </div>
    </body>
    """

if __name__ == '__main__':
    app.run(debug=True)