from fastapi import FastAPI

from acao import router as hash_acoes

app = FastAPI()

@app.get("/")
def root():
    return {"Hello":"World"}

app.include_router(hash_acoes, prefix="/acao", tags=["acao"])