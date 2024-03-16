from . import db
from sqlalchemy import Time

class Transporte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    linha = db.Column(db.String(80), nullable=False)
    origem = db.Column(db.String(80), nullable=False)
    destino = db.Column(db.String(80), nullable=False)
    horario = db.Column(Time, nullable=False)
    lotacao = db.Column(db.String(10), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "linha": self.linha,
            "origem": self.origem,
            "destino": self.destino,
            "horario": self.horario.strftime("%H:%M:%S") if self.horario else None,
            "lotacao": self.lotacao
        }
