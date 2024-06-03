from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import string
# import bd.base as bd
import json
import re

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


@app.get("/")
async def index():
    return "hola mundo!"


@app.post("/otro/")
async def otro(objeto: Item):

    correo = objeto.correo
    password = objeto.password

    

    # Access item_id from the URL path parameter
    return {"message": f"Received item ID: {correo}"}