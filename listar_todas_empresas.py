from bs4 import BeautifulSoup
import requests


from ativo_modelo import Acoes

acoes=''
url = 'https://www.dadosdemercado.com.br/acoes'
response=requests.get(url)
data=response.text
soup = BeautifulSoup(data, 'html.parser')

with open('list_acao.text', 'w') as arq:
    for body_table in soup.find_all('tbody'):
        for row_table in body_table.find_all('tr'):
            arq.writelines(row_table.find('a').text + '\n')