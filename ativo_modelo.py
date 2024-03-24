from pydantic import BaseModel
from datetime import datetime


class Ativo(BaseModel):
    codigo:str
    name:str
    liquidez:int
    variacao:float
    

class Acoes(Ativo):
    pass

class FIIs(Ativo):
    pass