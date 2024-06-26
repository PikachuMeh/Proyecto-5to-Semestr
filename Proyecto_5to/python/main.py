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
import pyautogui


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
    cedula: str
    clave: str
    pais: str
    estado: str
    roles_idroles: int
    token_idtoken: int
    recuperacion: str
    nacimiento: str
    desc_per: str
    x: str
    instagram: str
    facebook: str
    tik_tok : str

class consulta(BaseModel):
    correo: str

class recuperar(BaseModel):
    correo: str


@app.get("/")
async def index():
    return "hola mundo!"

@app.post("/consulta_todo/")
async def consulta(Correo : consulta):
    correo_electronico = Correo.correo
    datosx = session.query(usuarios).where(usuarios.correo == correo_electronico).first()

    if datosx:
        respuesta_json = {"datos": datosx}
    else:
        respuesta_json = {"mensaje": "No se encontraron datos para el correo electrónico especificado"}

    return respuesta_json

@app.post("/login/")
async def otro(objeto: Item):

    correo = objeto.correo
    password = objeto.password


    correox = session.query(usuarios).where(usuarios.correo == correo).first()


    if(correox == None or password != correox.clave):

        return {"Falso":False}

    else:

        return {"correo":correox}




@app.post("/registro")
async def registro(archivo : registro):


    # Aca ira toda la parte donde recopila la informacion
    correox = archivo.correo
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
    del tokens['cedula']
    del tokens['nacimiento']
    del tokens['desc_per']
    del tokens['x']
    del tokens['instagram']
    del tokens['facebook']
    del tokens['tik_tok']

    # Create an instance of the token class using the filtered tokens


    correo_reg = session.query(usuarios).where(usuarios.correo == correox).first()
    if(correo_reg == None):
        # Generar un correo cada vez que haga un registro
        token_instance = token(**tokens)

        # Add the token instance to the session
        session.add(token_instance)
        session.commit()

        token_bus = session.query(token).where(token.recuperacion == tokenx).first()

        nuevo_usuario = archivo.dict()
        del nuevo_usuario['recuperacion']
        del nuevo_usuario['x']
        del nuevo_usuario['instagram']
        del nuevo_usuario['facebook']
        del nuevo_usuario['tik_tok']

        nuevo_usuario['token_idtoken'] = token_bus.id_token

        usuario_instancia = usuarios(**nuevo_usuario)
        session.add(usuario_instancia)
        session.commit()

        red_social = archivo.dict()
        del red_social['nombre']
        del red_social['apellido']
        del red_social['correo']
        del red_social['clave']
        del red_social['pais']
        del red_social['estado']
        del red_social['roles_idroles']
        del red_social['token_idtoken']
        del red_social['cedula']
        del red_social['nacimiento']
        del red_social['desc_per']
        del red_social['recuperacion']

        social_instancia = redes_sociales(**red_social)
        session.add(social_instancia)
        session.commit()


        load_dotenv()
        password = os.getenv("PASSWORD")
        email_sender = "juanmalave.itjo@gmail.com"  # el que envia el correo

        email_reciver = correox #el que recibe el correo

        subject = "Registro de su cuenta"
        screenshot = pyautogui.screenshot()
        screenshot.save("../src/imagenes/captura_de_pantalla.png")
        screenshot.show()
        body = f"We received a request to recover your account. \n"
        body += f"Toma tu token de recuperacion:"
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
async def recuperacion(archivo:recuperar):

    correo_ver = archivo.correo
    correo_final = session.query(usuarios).where(usuarios.correo == correo_ver).first()

    if(correo_final == None):

        return {"False": False}
    else:
        load_dotenv()
        password = os.getenv("PASSWORD")
        email_sender = "juanmalave.itjo@gmail.com"  # el que envia el correo

        email_reciver = correo_ver  # el que recibe el correo

        subject = "Registro de su cuenta"

        body = f"We received a request to recover your account. \n"
        body += f"Esta es tu clave:"
        body += f"{correo_final.clave} \n"  # Replace with actual password reset link generation
        body += f"\nIf you didn't request a password reset, you can safely ignore this email."

        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = email_reciver
        em["Subject"] = subject
        em.set_content(body)

        contexto = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=contexto) as smtp:
            smtp.login(email_sender, password)
            smtp.sendmail(email_sender, email_reciver, em.as_string())
        return {"data": correo_final}