from pydantic import BaseModel
from datetime import datetime

class Paper(BaseModel):
    paper:str
    price:float
    time:datetime

class Acoes(Paper):
    pass

class FIIs(Paper):
    pass