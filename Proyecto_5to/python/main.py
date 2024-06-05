import os
from dotenv import load_dotenv
from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import string
import bd.base as bd
import json
import re
from bd.models.models import usuarios,token,roles
from email.message import EmailMessage
import ssl
import smtplib

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    correo: str
    password: str

class registro(BaseModel):
    nombre: str
    apellido: str
    correo: str
    password: str


@app.get("/")
async def index():
    return "hola mundo!"


@app.post("/login/")
async def otro(objeto: Item):

    correo = objeto.correo
    password = objeto.password


    dato = bd.session.query(usuarios).first()


    # Access item_id from the URL path parameter
    return {"message": f"Received item ID: {dato.nombre}"}


@app.post("/registro")
async def registro(archivo : registro):


    # Aca ira toda la parte donde recopila la informacion
    nombre = archivo.nombre
    apellido = archivo.apellido
    correo = archivo.correo
    clave = archivo.password

    # Generar un correo cada vez que haga un registro
    load_dotenv()
    password = os.getenv("PASSWORD")
    email_sender = "juanmalave.itjo@gmail.com"  # el que envia el correo

    email_reciver = correo #el que recibe el correo

    subject = "Registro de su cuenta"

    body = "Esto es un correo de prueba de mi proyecto de 5to SEMESTRE"

    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_reciver
    em["Subject"] = subject
    em.set_content(body)

    contexto = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=contexto) as smtp:
        smtp.login(email_sender,password)
        smtp.sendmail(email_sender,email_reciver,em.as_string())



    return {"nombre": nombre,"apellido": apellido,"correo":correo,"clave": clave}