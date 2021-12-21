from flask_login import UserMixin
from sqlalchemy.orm import backref, relationship
from cadastroUsuario.extensions.database import db
from sqlalchemy_serializer import SerializerMixin

class Usuario(db.Model, SerializerMixin, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    endereco = db.relationship("EnderecoUsuario", backref="Usuario", uselist=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    pis = db.Column(db.String(11), unique=True, nullable=False)
    senha = db.Column(db.String(512))

class EnderecoUsuario(db.Model, SerializerMixin, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), unique = True)
    pais = db.Column(db.String(80), nullable=False)
    estado = db.Column(db.String(80), nullable=False)
    municipio = db.Column(db.String(80), nullable=False)
    cep = db.Column(db.String(10), nullable=False)
    rua = db.Column(db.String(80), nullable=False)
    numero = db.Column(db.String(15))
    complemento = db.Column(db.String(80))