from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from database import init_db
from models import Mascotas, db

app = Flask(__name__)

# Configuración
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgre:1234@postgres:5432/mascotas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar DB y JWT
init_db(app)
jwt = JWTManager(app)

# Página de registro
@app.route('/adoptar', methods=['GET', 'POST'])
def adoptar_mascota():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        especie = request.form.get('especie')
        usuario_id = request.form.get('usuario_id')

        if not nombre or not especie or not usuario_id:
            return jsonify({"error": "Datos incompletos"}), 400

        nueva_mascota = Mascotas(
            nombre=nombre,
            especie=especie,
            usuario_id=usuario_id
        )

        db.session.add(nueva_mascota)
        db.session.commit()
        return redirect(url_for('adopcion_exitosa'))

    return render_template('adoptar.html')

@app.route('/mascotas/estado/<int:id>', methods=['GET'])
def obtener_estado(id):
    mascota = Mascotas.query.get(id)
    if not mascota:
        return jsonify({"error": "Mascota no encontrada"}), 404
    return jsonify(mascota.to_dict())

@app.route('/adopcion-exitosa', methods=['GET'])
def adopcion_exitosa():
    # Recomendaciones de cuidado según la especie

    cuidado = "Cuida mucho a tu nueva mascota y dale todo tu amor."
    return render_template('adopcion_exitosa.html', cuidado=cuidado)


# Ruta para listar las mascotas del usuario
@app.route('/mismascotas', methods=['GET'])
def listar_mascotas():
    usuario_id = 1  # Fijamos el user_id por defecto para esta implementación
    mascotas = Mascotas.query.filter_by(usuario_id=str(usuario_id)).all()
    return render_template('mismascotas.html', mascotas=mascotas)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)