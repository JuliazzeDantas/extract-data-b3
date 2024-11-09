from bs4 import BeautifulSoup
import requests


from ativo_modelo import Acoes

acoes=''
url = 'https://www.dadosdemercado.com.br/acoes'
response=requests.get(url)
data=response.text
soup = BeautifulSoup(data, 'html.parser')

with open('list_stock.text', 'w') as arq:
    for body_table in soup.find_all('tbody'):
        for row_table in body_table.find_all('tr'):
            arq.writelines(row_table.find('a').text + '\n')


with open("list_stock.text", 'r') as arq:
    stock_list = arq.read().lower().split()


for stock in stock_list:
    url=f'https://www.fundamentus.com.br/detalhes.php?papel=itub4'
    response=requests.get(url)
    data=response.text
    soup = BeautifulSoup(data, 'html.parser')
    data_json={stock:{}}

    for divs in soup.find_all('div', class_= "stock-details grid-m2-t3-d4"):
        print("divs")
        for stock_detail in divs.find_all('div', class_="ratio"):
            dict_title = stock_detail.find_all('span')[0].text
            value = stock_detail.find_all('span')[1].text.replace('.','').replace(',','.')
            if 'mi' in value:
                value = value.replace('\u202fmi', '')
                value = int(value)*1000000
            elif 'bi' in value:
                value = value.replace('\u202fbi', '')
                value = int(value)*1000000000
            elif "%" in value:
                value = value.replace('%','')
                value = float(value)/100
                value = round(value, 4)
            else: 
                value = float(value)
                value = round(value, 2)
            data_json[stock][dict_title] = value

    print(data_json)