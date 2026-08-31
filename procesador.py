from fastapi import FastAPI, UploadFile, File
import pandas as pd
import spacy

app = FastAPI()

# Cargar modelo grande de spaCy con vectores
nlp = spacy.load("es_core_news_lg")

@app.post("/analizar_excel")
async def analizar_excel(archivo: UploadFile = File(...)):
    # Leer Excel en DataFrame
    df = pd.read_excel(archivo.file)

    resultados = []

    # Procesar cada registro (ejemplo: columna 'texto')
    for texto in df["texto"].astype(str):
        doc = nlp(texto)

        # Entidades
        entidades = [(ent.text, ent.label_) for ent in doc.ents]

        # Similaridad ejemplo: comparar con palabra "salud"
        similitud_salud = doc.similarity(nlp("salud"))

        resultados.append({
            "texto": texto,
            "entidades": entidades,
            "similitud_salud": similitud_salud
        })

    return {"total_registros": len(resultados), "analisis": resultados[:50]}