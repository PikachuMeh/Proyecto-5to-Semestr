from ..base import Base
import datetime
from sqlalchemy import (Double, Table, Column, Integer, String, Text, CHAR, Boolean, Date, Time, TIMESTAMP, ForeignKey,Uuid, BigInteger )
from sqlalchemy.dialects.postgresql import BIT


class usuarios(Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer, primary_key=True,autoincrement=True,nullable=False)
    cedula = Column(Integer, nullable=False)
    password = Column(CHAR(20), nullable=False)
    nombre = Column(CHAR(50), nullable=False)
    apellido = Column(CHAR(50), nullable=False)
    email = Column(CHAR(150), nullable=False)
    Pais = Column(Text, nullable=False)
    estado = Column(Text, nullable=False)
    rolId_token = Column(Integer, ForeignKey("token.idToken"), primary_key=True, nullable=False)
    rolId = Column(Integer, ForeignKey("roles.idRoles"), primary_key=True, nullable=False)

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
