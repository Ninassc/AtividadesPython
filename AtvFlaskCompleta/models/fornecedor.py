from .base import ModeloBase
from . import db

class Fornecedor(ModeloBase):
    __tablename__ = "fornecedores"

    nome_empresa = db.Column(db.String(150), nullable=False)
    cnpj = db.Column(db.String(20), nullable=False)
    produto_fornecido = db.Column(db.String(150), nullable=False)
    
    @classmethod
    def listar_fornecedores(cls):
        return cls.query.order_by(cls.id).all()
    
    def salvar(self):
        db.session.add(self)
        db.session.commit()
