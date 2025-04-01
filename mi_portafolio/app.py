from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/proyecto')
def proyecto():
    return render_template('proyecto.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    # Puedes definir estas variables en tu entorno si deseas personalizar la IP y el puerto.
    host_ip = os.getenv("FLASK_HOST", "0.0.0.0")
    port = int(os.getenv("FLASK_PORT", 5000))
    
    app.run(debug=True, host=host_ip, port=port)  # No olvides que la IP es personal si vas a subir este código a un repo público
