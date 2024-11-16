from database import db
from datetime import datetime

class Interacciones(db.Model):
    __tablename__ = 'interacciones'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    fecha = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    mascota_id = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "fecha_adopcion": self.fecha_adopcion.strftime('%Y-%m-%d %H:%M:%S') if self.fecha_adopcion else None,
            "mascota_id": self.mascota_id,
        }
