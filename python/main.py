from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from forward_chaining_tanaman import forward_chaining, rules

app = FastAPI(
    title="Sistem Pakar Tanaman API",
    description="API untuk memberikan rekomendasi tanaman berdasarkan kondisi lahan menggunakan forward chaining",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class FactsInput(BaseModel):
    facts: list[str]

@app.post("/infer")
def infer_tanaman(input_data: FactsInput):
    inferred, explanations = forward_chaining(set(input_data.facts), rules)
    return {
        "facts_awal": input_data.facts,
        "fakta_akhir": list(inferred),
        "penjelasan": explanations
    }

@app.get("/")
def home():
    return {"message": "Sistem Pakar Tanaman API aktif. Gunakan endpoint /infer"}
