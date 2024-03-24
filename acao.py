from fastapi import APIRouter, HTTPException
from ativo_modelo import Acoes


hash_acoes:Acoes = {}
router = APIRouter()

@router.get("/")
def root():
    return hash_acoes

@router.get("/acoes/{paper}/price")
def get_currently_acoes_price(paper:str):
    try:
        return hash_acoes['paper'][-1]
    except:
        raise HTTPException(status_code=404, detail=f"A Ação {paper} não foi encontrada")

@router.post("/acoes")
def create_acao(paper:Acoes):
    if paper.paper in hash_acoes:
        if len(hash_acoes[paper.paper]) > 1825:
            hash_acoes[paper.paper].pop(0)
        hash_acoes[paper.paper].append(paper)
    else:
        hash_acoes[paper.paper]=[paper]

    return hash_acoes[paper.paper]

