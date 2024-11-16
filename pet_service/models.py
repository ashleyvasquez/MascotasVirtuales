from database import db
from datetime import datetime

class Mascotas(db.Model):
    __tablename__ = 'mascotas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    especie = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(50), nullable=True, default='feliz')  
    fecha_adopcion = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    usuario_id = db.Column(db.String(120), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "especie": self.especie,
            "estado": self.estado,
            "fecha_adopcion": self.fecha_adopcion.strftime('%Y-%m-%d %H:%M:%S') if self.fecha_adopcion else None,
            "usuario_id": self.usuario_id,
        }
