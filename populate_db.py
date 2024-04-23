from scrape_data import Scraper
from ativo_modelo import Ativo
from datetime import datetime

scraper=Scraper()
hash_table_acoes={}

list_fii=[]

with open('list_ativos.txt', 'r') as arq:
    list_acoes=arq.read().split('\n')
arq.close()

for acao in list_acoes:
    if (acao in hash_table_acoes) == False:
        hash_table_acoes[acao]={}
    try:
        scraper.set_url_acao(acao)
        paper_data=scraper.get_acao(acao)
        #print(acao)
        hash_table_acoes[acao]=paper_data
    except:
        list_fii.append(acao)
        print(acao)

with open('list_fiis.txt', 'w') as arq:
    for fii in list_fii:
        arq.writelines(fii + '\n')
arq.close()


