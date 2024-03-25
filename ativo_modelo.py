from pydantic import BaseModel
from datetime import datetime


class Ativo(BaseModel):
    codigo:str
    name:str
    #liquidez:int
    #variacao:float
    currently_price:float
    dividend_yield:float
    pl:float
    peg_ratio:float
    pvp:float
    ev_ebitda:float
    ev_ebit:float
    p_ebitda:float
    p_ebit:float
    vpa:float
    p_ativo:float
    lpa:float
    p_sr:float
    p_cap_giro:float
    p_ativo_circ_liq:float

    def set_codigo(self, code):
        self.codigo=code
    

class Acoes(Ativo):
    pass

class FIIs(Ativo):
    pass