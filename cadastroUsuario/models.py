from enum import unique
from flask_login import UserMixin
from sqlalchemy.orm import backref, relationship
from cadastroUsuario.extensions.database import db
from sqlalchemy_serializer import SerializerMixin

class Usuario(db.Model, SerializerMixin, UserMixin):
    __tablename__ = 'Usuario'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    pis = db.Column(db.String(11), unique=True, nullable=False)
    senha = db.Column(db.String(512))
    
    def __repr__(self):
        return self.name

    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_by_id(cls,id):
        return cls.query.get_or_404(id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class EnderecoUsuario(db.Model, SerializerMixin, UserMixin):
    __tablename__ = 'EnderecoUsuario'
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('Usuario.id'))
    usuario = db.relationship("Usuario", backref="EnderecoUsuario")
    pais = db.Column(db.String(80), nullable=False)
    estado = db.Column(db.String(80), nullable=False)
    municipio = db.Column(db.String(80), nullable=False)
    cep = db.Column(db.String(10), nullable=False)
    rua = db.Column(db.String(80), nullable=False)
    numero = db.Column(db.String(15))
    complemento = db.Column(db.String(80))
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    def save(self):
            db.session.add(self)
            db.session.commit()