from database import db
import bcrypt

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.LargeBinary, nullable=False)

    def set_password(self, raw_password):
        # Genera el hash de la contraseña y lo guarda como binario
        self.password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, raw_password):
        # Valida la contraseña comparándola con el hash almacenado usando bcrypt
        return bcrypt.checkpw(raw_password.encode('utf-8'), self.password)
