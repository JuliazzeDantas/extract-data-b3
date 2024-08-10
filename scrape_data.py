from bs4 import BeautifulSoup
import requests

from datetime import datetime
import json



stock='itub4'

url='https://www.fundamentus.com.br/detalhes.php?papel=itub4'
response=requests.get(url)
data=response.text
soup = BeautifulSoup(data, 'html.parser')
data_json={stock:{}}

print(soup)

for divs in soup.find_all('div', class_= "stock-details grid-m2-t3-d4"):
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