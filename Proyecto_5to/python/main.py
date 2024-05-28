from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173/",
    "http://localhost:8000",
    "https://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def inicio():
    return "hola mundo!"

@app.get("/otro")
async def otro():
    dato = 1
    #dato = bd.session.query(maestros).first()
    return {"maestros": dato}
