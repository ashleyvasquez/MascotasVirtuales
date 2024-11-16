from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from database import init_db
from models import Interacciones, db

app = Flask(__name__)

# Configuración
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgre:1234@postgres:5432/mascotas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar DB y JWT
init_db(app)
jwt = JWTManager(app)

# Página de registro
@app.route('/interaccion', methods=['GET', 'POST'])
def interactuar_mascota():
    if request.method == 'POST':
        mascota_id = request.form.get('mascota_id')
        tipo = request.form.get('tipo')

        nueva_interaccion = Interacciones(
            mascota_id=mascota_id,
            tipo=tipo,
        )

        db.session.add(nueva_interaccion)
        db.session.commit()
        return redirect(url_for('interaccion_exitosa'))

    return render_template('interaccion.html')

@app.route('/interaccion_exitosa', methods=['GET'])
def interaccion_exitosa():
    return render_template('interaccion_exitosa.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)