from bs4 import BeautifulSoup as bs4

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from ativo_modelo import Acoes

acoes=''

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)
wait = WebDriverWait(driver, 10)

url='https://www.infomoney.com.br/cotacoes/empresas-b3/'

driver.get(url)
amontado_de_tabelas=driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]') # Acha o local onde as tabelas estão
list_table=amontado_de_tabelas.find_elements(By.CLASS_NAME, 'list-companies') # Faz uma lista das tabelas que existem no site

with open('lista_acoes.text', 'w') as arq: 
    for area in list_table: #Faz um loop para cada uma das tabelas

        soup=bs4(area.get_attribute("innerHTML"), 'html.parser')
        strong_elements = soup.find_all(class_='strong')   # Usa o bs4 para pegar o corpo html das tabelas 

        for element in strong_elements: # Pega linha por linha da tabela
            a_tag = element.find('a')
            if a_tag is not None:
                papel=a_tag.text.strip()
                if len(papel) == 0:
                    arq.write('SOJA3\n')
                elif papel[-1].strip()!='F':
                    arq.write(papel.strip()+'\n')              

arq.close()