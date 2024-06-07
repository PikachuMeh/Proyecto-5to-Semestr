from ..base import Base
import datetime
from sqlalchemy import (Double, Table, Column, Integer, String, Text, CHAR, Boolean, Date, Time, TIMESTAMP, ForeignKey,Uuid, BigInteger )
from sqlalchemy.dialects.postgresql import BIT



class usuarios(Base):
    __tablename__ = "usuarios"
    id_usuarios = Column(Integer, primary_key=True,autoincrement=True,nullable=False)
    cedula = Column(Integer, nullable=False)
    clave = Column(CHAR(20), nullable=False)
    nombre = Column(CHAR(50), nullable=False)
    apellido = Column(CHAR(50), nullable=False)
    correo = Column(CHAR(150), nullable=False)
    pais = Column(Text, nullable=False)
    estado = Column(Text, nullable=False)
    roles_idroles = Column(Integer, ForeignKey("roles.idRoles"), primary_key=True, nullable=False)
    token_idtoken = Column(Integer, ForeignKey("token.idToken"), primary_key=True, nullable=False)


class token(Base):
    __tablename__ = "token"
    id_token = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    recuperacion = Column(CHAR(45),nullable=False)

class roles(Base):
    __tablename__ = "roles"
    id_rol = Column(Integer,primary_key=True,nullable=False)
    administrador = Column(Boolean)
    visitante = Column(Boolean)
    visualizacion = Column(Boolean)
    usuarios_id = (Integer,ForeignKey("usuario.id_usuario"))

class redes_sociales(Base):
    __tablename__ = "redes_sociales"
    id_Redes_sociales = Column(Integer, primary_key=True, nullable=False,autoincrement=True)
    x = Column(CHAR(50),nullable=False)
    Instagram = Column(CHAR(50),nullable=False)
    Tik_tok = Column(CHAR(50),nullable=False)
    Facebook = Column(CHAR(50),nullable=False)

class redes_sociales_aux(Base):
    __tablename__ = "usuarios_has_redes_sociales"
    usuarios_id_usuarios = Column(Integer,ForeignKey("usuarios.id_usuario"), primary_key=True)
    usuarios_roles_idroles = Column(Integer,ForeignKey("usuarios.roles_idroles"),primary_key=True)
    redes_Sociales_idRedes_Sociales = Column(Integer,ForeignKey("redes_sociales.id_Redes_sociales"), primary_key=True)
