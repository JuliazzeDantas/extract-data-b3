from scrape_data import Scraper

with open('lists/list_acao.txt', 'r') as arq:
    acoes = arq.readlines()

arq.close()

acoes = [acao.strip() for acao in acoes]
print(acoes)

scraper = Scraper()

with open('lists/list_acao.txt', 'r') as arq:
    acoes = arq.readlines()

arq.close()

acoes = [acao.strip() for acao in acoes]
print(acoes)

print(scraper.get_acao_valuation('WEGE3'))