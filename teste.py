# Importar bibliotecas que serão usadas
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime

# Configurando o browser
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless")  # Executa o Chrome em modo headless (sem interface gráfica)

driver = webdriver.Chrome(service = service, options=options)
wait = WebDriverWait(driver, 10)

# Definir variáveis auxiliares
row = 1
item = 1
url = 'https://www.freitasleiloeiro.com.br/Leiloes/Pesquisar?query=&categoria=1'
url_teste_button = 'https://www.freitasleiloeiro.com.br/Leiloes/Pesquisar?Categoria=1&Nome=&TipoLoteId=3&AnoModeloMin=0&AnoModeloMax=0&Condicao=inteiros&PatioId=0&FaixaValor=1'

# Definir os Caminhos
xpath_button_carregar_mais = '/html/body/main/div[2]/div/div[2]/div[3]/button' # Pesquisar até dar disabled
xpath_corpo_lista_item = '/html/body/main/div[2]/div/div[2]/div[2]'
xpath_lista_itens = f'/html/body/main/div[2]/div/div[2]/div[2]/div[{row}]'

#Talvez eu busque esse itens depois de passar item para uma variável. Assim, não precisara desse "xpath_itens" na frente das variáveis
xpath_itens = xpath_lista_itens + f'/div[{item}]' # /html/body/main/div[2]/div/div[2]/div[2]/div[{row}]/div[{item}]
xpath_data_leilao = xpath_itens + '/div/div[3]/div[1]/span[1]' # f'/html/body/main/div[2]/div/div[2]/div[2]/div[3]/div[{item}]/div/div[3]/div[1]/span[1]'
xpath_horario_leilao = xpath_itens + '/div/div[3]/div[1]/span[2]'
xpath_info_carro = xpath_itens + '/div/div[3]/div[2]/span'
xpath_opcionais = xpath_itens + '/div/div[3]/div[3]' # Lista de itens de opcionais
xpath_item_opcional = '/button[1]/span' # procurar dentro dos opcionais 

# Processo de scraping
driver.get(url_teste_button)
