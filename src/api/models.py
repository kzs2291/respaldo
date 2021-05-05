from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Usuarios(db.Model):
    __tablename__ = 'Usuarios'
    USUARIO_ID = db.Column(db.Integer, primary_key=True)
    USUARIO_EMAIL = db.Column(db.String(120), unique=True, nullable=False)
    USUARIO_PASSWORD = db.Column(db.String(80), unique=False, nullable=False)
    USUARIO_IS_ACTIVE = db.Column(db.Boolean(), unique=False, nullable=False)
    def __repr__(self):
        return '<Usuario %r>' % self.USUARIO_EMAIL

    def serialize(self):
        return {
            "id": self.USUARIO_ID,
            "email": self.USUARIO_EMAIL,
            # do not serialize the password, its a security breach
        }

class Empresa(db.Model):
    __tablename__ = 'Empresa'
    EMPRESA_ID = db.Column(db.Integer, primary_key=True)
    EMPRESA_NOMBRE = db.Column(db.String(120), unique=True, nullable=False)
    EMPRESA_UBICACION = db.Column(db.String(120), unique=False, nullable=True)
    EMPRESA_TELEFONO = db.Column(db.String(10), unique=False, nullable=True)
    EMPRESA_CELULAR = db.Column(db.String(10), unique=False, nullable=True)
    EMPRESA_DESCRIPCION= db.Column(db.String(200), unique=False, nullable=True)
    EMPRESA_LATITUD = db.Column(db.String(50), unique=False, nullable=True)
    EMPRESA_LONGITUD = db.Column(db.String(50), unique=False, nullable=True)
    EMPRESA_OTROS = db.Column(db.String(120), unique=False, nullable=True)
    EMPRESA_FOTO_FONDO = db.Column(db.String(120), unique=False, nullable=True)
    EMPRESA_LOGO = db.Column(db.String(120), unique=False, nullable=True)
    def __repr__(self):
        return '<Empresa %r>' % self.EMPRESA_NOMBRE

    def serialize(self):
        return {
            # do not serialize the password, its a security breach
            "ID": self.EMPRESA_ID,
            "NOMBRE": self.EMPRESA_NOMBRE,
            "UBICACION": self.EMPRESA_UBICACION,
            "TELEFONO": self.EMPRESA_TELEFONO,
            "CELULAR": self.EMPRESA_CELULAR,
            "DESCRIPCION": self.EMPRESA_DESCRIPCION,
            "LATITUD": self.EMPRESA_LATITUD,
            "LONGITUD": self.EMPRESA_LONGITUD,
            "OTROS": self.EMPRESA_OTROS,
            "FOTO_FONDO": self.EMPRESA_FOTO_FONDO,
            "LOGO": self.EMPRESA_LOGO,
        } 
class Empresa_Anuncios(db.Model):
    __tablename__ = 'Anuncios'
    ANUNCIO_ID = db.Column(db.Integer, primary_key=True)    
    ANUNCIO_NOMBRE = db.Column(db.String(120), unique=False, nullable=False)
    ANUNCIO_DESCRIPCION = db.Column(db.String(200), unique=False, nullable=True)
    ANUNCIO_FOTO_FONDO = db.Column(db.String(120), unique=False, nullable=True)
    EMPRESA_ID = db.Column(db.Integer,db.ForeignKey('Empresa.EMPRESA_ID'))
    Empresa = db.relationship(Empresa)
    def __repr__(self):
        return '<Anuncio %r>' % self.ANUNCIO_NOMBRE

    def serialize(self):
        return {           
            "ID": self.ANUNCIO_ID,   
            "NOMBRE": self.ANUNCIO_NOMBRE,
            "DESCRIPCION": self.ANUNCIO_DESCRIPCION,
            "FOTO_FONDO": self.ANUNCIO_FOTO_FONDO,          
        }


class Actividades (db.Model):
    __tablename__ = 'Actividades'
    ACTIVIDAD_ID = db.Column(db.Integer, primary_key=True)     
    ACTIVIDAD_NOMBRE = db.Column(db.String(120), unique=False, nullable=False)
    ACTIVIDAD_ENTRENADOR = db.Column(db.String(120), unique=False, nullable=True)
    ACTIVIDAD_LUGAR = db.Column(db.String(120), unique=False, nullable=True)
    ACTIVIDAD_PRECIO = db.Column(db.Integer, unique=False, nullable=True)
    ACTIVIDAD_ESPACIOS = db.Column(db.Integer, unique=False, nullable=True)
    ACTIVIDAD_ESPACIOS_DISPONIBLES = db.Column(db.Integer, unique=False, nullable=True)
    ACTIVIDAD_DESCRIPCION = db.Column(db.String(200), unique=False, nullable=True)
    ACTIVIDAD_ESTADO = db.Column(db.String(15), unique=False, nullable=True)
    ACTIVIDAD_DIA_SEMANA = db.Column(db.String(10), unique=False, nullable=True)
    ACTIVIDAD_FECHA_INICIO = db.Column(db.Date, default=datetime.today())
    ACTIVIDAD_HORA_INICIO = db.Column(db.String(30), unique=False, nullable=True)
    ACTIVIDAD_DURACION = db.Column(db.Integer, unique=False, nullable=True)
    ACTIVIDAD_FOTO = db.Column(db.String(120), unique=False, nullable=True)
    EMPRESA_ID = db.Column(db.Integer,db.ForeignKey('Empresa.EMPRESA_ID'))
    Empresa_Anuncios = db.relationship(Empresa)
    def __repr__(self):
        return '<Actividad %r>' % self.ACTIVIDAD_NOMBRE

    def serialize(self):
        return {            
            "ID": self.ACTIVIDAD_ID,
            "NOMBRE": self.ACTIVIDAD_NOMBRE,
            "ENTRENADOR": self.ACTIVIDAD_ENTRENADOR,
            "LUGAR": self.ACTIVIDAD_LUGAR,
            "PRECIO": self.ACTIVIDAD_PRECIO,
            "ESPACIOS": self.ACTIVIDAD_ESPACIOS,
            "ESPACIOS_DISPONIBLES": self.ACTIVIDAD_ESPACIOS_DISPONIBLES,
            "DESCRIPCION": self.ACTIVIDAD_DESCRIPCION,
            "ESTADO": self.ACTIVIDAD_ESTADO,
            "DIA_SEMANA": self.ACTIVIDAD_DIA_SEMANA,
            "FECHA_INICIO": self.ACTIVIDAD_FECHA_INICIO,
            "HORA_INICIO": self.ACTIVIDAD_HORA_INICIO,
            "DURACION": self.ACTIVIDAD_DURACION, 
            "FOTO": self.ACTIVIDAD_FOTO,
        }

class Actividades_Participantes(db.Model):
    __tablename__ = 'Participantes'
    LISTA_ID = db.Column(db.Integer, primary_key=True)
    ACTIVIDAD_ID = db.Column(db.Integer,db.ForeignKey('Actividades.ACTIVIDAD_ID'))
    Actividades = db.relationship(Actividades)
    PERSONA_ID = db.Column(db.Integer,db.ForeignKey('Usuarios.USUARIO_ID'))
    Usuarios = db.relationship(Usuarios)
    def __repr__(self):
        return '<Participante %r>' % self.PERSONA_ID

    def serialize(self):
        return {            
            "LISTA": self.LISTA_ID,
            "ACTIVIDAD": self.ACTIVIDAD_ID,
            "PERSONA": self.PERSONA_ID,

        }