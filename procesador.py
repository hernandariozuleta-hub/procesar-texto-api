from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class Entrada(BaseModel):
    texto: str
    repetir: bool = False

@app.post("/procesar_texto")
async def procesar_texto(data: Entrada):
    resultado = data.texto.upper() if data.repetir else data.texto.lower()
    return {"resultado": resultado}
