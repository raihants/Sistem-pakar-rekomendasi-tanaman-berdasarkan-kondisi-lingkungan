from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tanaman.router import router as tanaman_router

app = FastAPI(
    title="Sistem Pakar API",
    description="API utama untuk berbagai sistem pakar",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Daftarkan router tanaman
app.include_router(tanaman_router)

@app.get("/")
def root():
    return {"message": "Sistem Pakar API aktif. Coba akses /tanaman atau API lain."}
