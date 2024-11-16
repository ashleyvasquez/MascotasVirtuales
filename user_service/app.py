from flask import Flask, render_template, request, jsonify, redirect, url_for, make_response
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from database import init_db
from models import Usuario, db

app = Flask(__name__)

# Configuración
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgre:1234@postgres:5432/mascotas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configurar el nombre de la cookie de acceso y leerla desde allí
app.config['JWT_COOKIE_NAME'] = 'access_token_cookie'
app.config['JWT_TOKEN_LOCATION'] = ['cookies']

# Inicializar DB y JWT
init_db(app)
jwt = JWTManager(app)

# Página de registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            return render_template('register.html', message="Completa todos los campos.")

        if Usuario.query.filter_by(username=username).first():
            return render_template('register.html', message="El usuario ya existe.")

        new_user = Usuario(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')

# Página de inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = Usuario.query.filter_by(username=username).first()
        
        # Si el usuario no existe o la contraseña es incorrecta
        if not user or not user.check_password(password):
            return jsonify({"msg": "Credenciales inválidas."}), 401  # Respuesta en formato JSON con error 401

        # Crear el token de acceso
        access_token = create_access_token(identity=username)

        # Crear la respuesta y establecer la cookie con el token
        response = make_response(redirect(url_for('protected')))
        response.set_cookie('access_token_cookie', access_token, httponly=True, secure=False, samesite='Strict')

        return response  # Redirigir al área protegida

    # Si es un GET, retornar el formulario de login (HTML)
    return render_template('login.html')

# Página protegida
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return render_template('protected.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
