from fastapi import APIRouter
from pydantic import BaseModel
from .inferred_engine_tanamin import forward_chaining
from .rules import rules

router = APIRouter(prefix="/tanaman", tags=["Tanaman"])

class FactsInput(BaseModel):
    facts: list[str]

@router.post("/infer")
def infer_tanaman(input_data: FactsInput):
    inferred, explanations = forward_chaining(set(input_data.facts), rules)
    return {
        "facts_awal": input_data.facts,
        "fakta_akhir": list(inferred),
        "penjelasan": explanations
    }

@router.get("/")
def home():
    return {"message": "Endpoint API Tanaman aktif"}
