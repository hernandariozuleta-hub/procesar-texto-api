from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class EntradaTexto(BaseModel):
    texto: str
    repetir: bool

@app.post("/procesar_texto")
def procesar_texto(datos: EntradaTexto):
    resultado = datos.texto.upper() if datos.repetir else datos.texto
    return {"resultado": resultado}

# Nuevo modelo para la suma
class Numeros(BaseModel):
    a: float
    b: float

@app.post("/sumar")
def sumar_numeros(datos: Numeros):
    resultado = datos.a + datos.b
    return {"suma": resultado}
