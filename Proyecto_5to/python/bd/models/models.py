from ..base import engine,Base
import datetime
from sqlalchemy import (Double, Table, Column, Integer, String, Text, CHAR, Boolean, Date, Time, TIMESTAMP, ForeignKey,Uuid, BigInteger )
from sqlalchemy.dialects.postgresql import BIT


class usuarios(Base):
    __tablename__ = "usuarios"
    id_usuarios = Column(Integer, primary_key=True,autoincrement=True,nullable=False)
    cedula = Column(CHAR(11), nullable=False)
    nacimiento = Column(CHAR(20),nullable=False)
    clave = Column(CHAR(20), nullable=False)
    nombre = Column(CHAR(50), nullable=False)
    apellido = Column(CHAR(50), nullable=False)
    correo = Column(CHAR(150), nullable=False)
    pais = Column(Text, nullable=False)
    estado = Column(Text, nullable=False)
    desc_per = Column(Text,nullable=False)
    roles_idroles = Column(Integer, ForeignKey("roles.id_rol"), nullable=False)
    token_idtoken = Column(Integer, ForeignKey("token.id_token"), nullable=False)


class token(Base):
    __tablename__ = "token"
    id_token = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    recuperacion = Column(CHAR(45),nullable=False)

class roles(Base):
    __tablename__ = "roles"
    id_rol = Column(Integer,primary_key=True,nullable=False)
    descripcion = Column(Text,nullable=False)

class redes_sociales(Base):
    __tablename__ = "redes_sociales"
    id_redes_sociales = Column(Integer, primary_key=True, nullable=False,autoincrement=True)
    x = Column(CHAR(50),nullable=False)
    instagram = Column(CHAR(50),nullable=False)
    tik_tok = Column(CHAR(50),nullable=False)
    facebook = Column(CHAR(50),nullable=False)

class redes_sociales_aux(Base):
    __tablename__ = "usuarios_has_redes_sociales"
    usuarios_id_usuarios = Column(Integer,ForeignKey("usuarios.id_usuario"), primary_key=True)
    redes_Sociales_idRedes_Sociales = Column(Integer,ForeignKey("redes_sociales.id_Redes_sociales"), primary_key=True)