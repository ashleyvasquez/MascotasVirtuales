from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)

# Configuración
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgre:1234@postgres:5432/mascotas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar DB y JWT
jwt = JWTManager(app)


@app.route('/')
def menu():
    return render_template('menu.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

