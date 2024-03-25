from scrape_data import Scraper
from ativo_modelo import Ativo
from datetime import datetime

scraper=Scraper()
hash_table_acoes={}

list_fii=[]

with open('lista_acoes.txt', 'r') as arq:
    list_acoes=arq.read().split('\n')
arq.close()

for acao in list_acoes:
    if (acao in hash_table_acoes) == False:
        hash_table_acoes[acao]={}
    print(acao)
    try:
        scraper.set_url_acao(acao)
        paper={datetime.now():{

            }
        }

        paper_data={
            datetime.now().strftime("%Y-%m-%d-%H-%M"):{
                "codigo":acao,
                "empresa":scraper.get_name(),
                "currently_price":scraper.get_currently_price(),
                "dividend_yield":scraper.get_dividend_yield(),
                "pl":scraper.get_pl(),
                "peg_ratio":scraper.get_peg_ratio(),
                "pvp":scraper.get_pvp(),
                "ev_ebitda":scraper.get_ev_ebitda(),
                "ev_ebit":scraper.get_ev_ebit(),
                "p_ebitda":scraper.get_p_ebitda(),
                "p_ebit":scraper.get_p_ebit(),
                "vpa":scraper.get_vpa(),
                "p_ativo":scraper.get_p_ativo(),
                "lpa":scraper.get_lpa(),
                "p_sr":scraper.get_p_sr(),
                "p_cap_giro":scraper.get_p_cap_giro(),
                "p_ativo_circ_liq":scraper.get_p_ativo_circ_liq()
            }
        }
        hash_table_acoes[acao]=paper_data
        print(hash_table_acoes)
    except:
        list_fii.append(acao)
