import configparser
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


config = configparser.ConfigParser()
config.read("config.ini")

usuario = config["BD"]["Usuario"]
password = config["BD"]["Password"]
ruta = config["BD"]["Ruta"]
puerto = config["BD"]["Puerto"]

nombre_bd = "bd_uestadal_poa"

engine = create_engine(f"postgresql+psycopg://{usuario}:{password}@{ruta}:{puerto}/{nombre_bd}")

Session = sessionmaker(bind=engine)
session = Session()

session.autobegin = True
session.autoflush = True

Base = declarative_base()
