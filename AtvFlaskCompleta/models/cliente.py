from .base import ModeloBase
from . import db

class Cliente(ModeloBase):
    __tablename__ = "clientes"

    nome = db.Column(db.String(150), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    pontos_fidelidade = db.Column(db.Integer, nullable=False)

    @classmethod
    def listar_clientes(cls):
        return cls.query.order_by(cls.id).all()
    
    def salvar(self):
        db.session.add(self)
        db.session.commit()
