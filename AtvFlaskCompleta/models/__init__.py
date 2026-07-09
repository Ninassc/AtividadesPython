from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .base import ModeloBase
from .cliente import Cliente
from .fornecedor import Fornecedor

__all__ = ['db', 'Cliente', 'Fornecedor', 'ModeloBase']