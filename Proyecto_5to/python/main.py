import os
from dotenv import load_dotenv
from typing import Union
from pydantic import BaseModel,Field
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from bd.base import Base,session
import string
import json
import re
from bd.models.models import usuarios,token,roles,redes_sociales,redes_sociales_aux
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
    clave: str
    pais: str
    estado: str
    roles_idroles: int
    token_idtoken: int
    recuperacion: str


@app.get("/")
async def index():
    return "hola mundo!"


@app.post("/login/")
async def otro(objeto: Item):

    correo = objeto.correo
    password = objeto.password


    dato = Base.session.query(usuarios).first()


    # Access item_id from the URL path parameter
    return {"message": f"Received item ID: {dato.nombre}"}




@app.post("/registro")
async def registro(archivo : registro):


    # Aca ira toda la parte donde recopila la informacion
    correo = archivo.correo
    tokenx = archivo.recuperacion
    tokens = archivo.dict()
    del tokens['nombre']
    del tokens['apellido']
    del tokens['correo']
    del tokens['clave']
    del tokens['pais']
    del tokens['estado']
    del tokens['roles_idroles']
    del tokens['token_idtoken']

    # Create an instance of the token class using the filtered tokens


    correo_reg = session.query(usuarios).where(usuarios.correo == correo).first()
    if(correo_reg == None):
        # Generar un correo cada vez que haga un registro
        token_instance = token(**tokens)

        # Add the token instance to the session
        session.add(token_instance)
        session.commit()

        token_bus = session.query(token).where(token.recuperacion == tokenx).first()

        nuevo_usuario = archivo.dict()
        del nuevo_usuario['recuperacion']

        nuevo_usuario['token_idtoken'] = token_bus.id_token

        usuario_instancia = usuarios(**nuevo_usuario)
        session.add(usuario_instancia)
        session.commit()
        load_dotenv()
        password = os.getenv("PASSWORD")
        email_sender = "juanmalave.itjo@gmail.com"  # el que envia el correo

        email_reciver = correo #el que recibe el correo

        subject = "Registro de su cuenta"

        body = f"We received a request to recover your account. \n"
        body += f"Click on the following link to reset your password: "
        body += f"{token_bus.recuperacion} \n"  # Replace with actual password reset link generation
        body += f"\nIf you didn't request a password reset, you can safely ignore this email."

        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = email_reciver
        em["Subject"] = subject
        em.set_content(body)

        contexto = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com",465,context=contexto) as smtp:
              smtp.login(email_sender,password)
              smtp.sendmail(email_sender,email_reciver,em.as_string())

        return {"Registro Completo"}

    else:
        return {"falso": False}
@app.post("/recuperacion")
async def recuperacion(archivo : registro):
    return 0