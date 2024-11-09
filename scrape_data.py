# Imports do Selenium e WebDriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Tentativa futura de fazer Proxy
from selenium.webdriver.common.proxy import Proxy, ProxyType # Olhar configuração de proxy caso o script volte a ser barrado no modo headless

# Bibliotecas auxiliares
import time
from datetime import datetime

# Imports para o Banco de Dados
import json
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='seu_usuario',
    password='sua_senha',
    database='seu_banco_de_dados'
)

#xpath_botao_fechar_anuncio = '/html/body/div[19]/div//section/div/div/div/div[2]/button'
#xpath_verificador_anuncio = '/html/body/div[27]/div//section/div/div/div'  # if style = flex: fecha anuncio.  flex -> none

class Scraper():

    driver:webdriver.Chrome
    service:Service
    wait:WebDriverWait

    url='https://statusinvest.com.br/acoes/wege3'

    def __init__(self):
        # Configura Options para o selelnium rodar em modo headless
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--headless=new")
        self.options.add_argument("ignore-certificate-errors")
        self.options.add_argument("--start-fullscreen")
        self.options.add_argument("--disable-logging")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36")

        # Instala o driver do Chrome e inicia o Browser
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service = self.service, options=self.options)
        self.wait = WebDriverWait(self.driver, 10)

        self.get_url(self.url)

    def get_url(self, url):
        self.driver.get(url)

    def set_url_acao(self, acao):
        url_acao='https://statusinvest.com.br/acoes/wege3'
        self.get_url(url_acao)


    def format_data_number(self, value):
        if (value=='-') or ((value=='-%')):
            return None
        else:
            if "%" in value:
                return float(value.replace('%', '').replace(',', '.'))/100
            else:
                return float(value.replace(',', '.'))
            

    def get_name(self):
        xpath_name='/html/body/main/header/div[2]/div/div[1]/h1/small'
        return self.driver.find_element(By.XPATH, xpath_name).text


    # Indicadores de Valuation
    def get_currently_price(self):
        xpath_price='/html/body/main/div[2]/div/div[1]/div/div[1]/div/div[1]/strong'
        value=self.driver.find_element(By.XPATH, xpath_price).text
        return self.format_data_number(value)


    def get_dividend_yield(self):
        xpath_dividend_yield='/html/body/main/div[2]/div/div[8]/div[2]/div/div[1]/div/div[1]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_dividend_yield).text
        return self.format_data_number(value)
    

    def get_pl(self):
        xpath_pl='/html/body/main/div[2]/div/div[8]/div[2]/div/div[1]/div/div[2]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_pl).text
        return self.format_data_number(value)
    

    def get_peg_ratio(self):
        xpath_peg_ratio='/html/body/main/div[2]/div/div[8]/div[2]/div/div[1]/div/div[3]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_peg_ratio).text
        return self.format_data_number(value)
  
    
    def get_pvp(self):
        xpath_pvp='/html/body/main/div[2]/div/div[8]/div[2]/div/div[1]/div/div[4]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_pvp).text
        return self.format_data_number(value)
    

    def get_ev_ebitda(self):
        xpath_ev_ebitda='/html/body/main/div[2]/div/div[8]/div[2]/div/div[1]/div/div[5]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_ev_ebitda).text
        return self.format_data_number(value)
    
    
    def get_ev_ebit(self):
        xpath_ev_ebit='/html/body/main/div[2]/div/div[8]/div[2]/div/div[1]/div/div[6]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_ev_ebit).text
        return self.format_data_number(value)
    

    def get_p_ebitda(self):
        xpath_p_ebitda='/html/body/main/div[2]/div/div[8]/div[2]/div/div[1]/div/div[7]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_p_ebitda).text
        return self.format_data_number(value)
    
    
    def get_p_ebit(self):
        xpath_p_ebit='/html/body/main/div[2]/div/div[8]/div[2]/div/div[1]/div/div[8]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_p_ebit).text
        return self.format_data_number(value)


    def get_vpa(self):
        xpath_vpa='/html/body/main/div[2]/div/div[8]/div[2]/div/div[1]/div/div[9]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_vpa).text
        return self.format_data_number(value)
    

    def get_p_ativo(self):
        xpath_p_ativo='/html/body/main/div[2]/div/div[8]/div[2]/div/div[1]/div/div[10]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_p_ativo).text
        return self.format_data_number(value)
    

    def get_lpa(self):
        xpath_lpa='/html/body/main/div[2]/div/div[8]/div[2]/div/div[1]/div/div[11]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_lpa).text
        return self.format_data_number(value)


    def get_p_sr(self):
        xpath_p_sr='/html/body/main/div[2]/div/div[8]/div[2]/div/div[1]/div/div[12]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_p_sr).text
        return self.format_data_number(value)


    def get_p_cap_giro(self):
        xpath_p_cap_giro='/html/body/main/div[2]/div/div[8]/div[2]/div/div[1]/div/div[13]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_p_cap_giro).text
        return self.format_data_number(value)


    def get_p_ativo_circ_liq(self):
        xpath_p_ativo_circ_liq='/html/body/main/div[2]/div/div[8]/div[2]/div/div[1]/div/div[14]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_p_ativo_circ_liq).text
        return self.format_data_number(value)

    
    # Indicadores de endividamento
    def get_div_liq_pl(self):
        xpath_div_liq_patri_liq='/html/body/main/div[2]/div/div[8]/div[2]/div/div[2]/div/div[1]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_div_liq_patri_liq).text
        return self.format_data_number(value)
    

    def get_div_liq_ebitda(self):
        xpath_div_liq_ebitda='/html/body/main/div[2]/div/div[8]/div[2]/div/div[2]/div/div[2]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_div_liq_ebitda).text
        return self.format_data_number(value)
    

    def get_div_liq_ebit(self):
        xpath_div_liq_ebit='/html/body/main/div[2]/div/div[8]/div[2]/div/div[2]/div/div[3]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_div_liq_ebit).text
        return self.format_data_number(value)

    
    def get_patri_liq_ativos(self):
        xpath_patri_liq_ativos='/html/body/main/div[2]/div/div[8]/div[2]/div/div[2]/div/div[4]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_patri_liq_ativos).text
        return self.format_data_number(value)


    def get_passivo_ativo(self):
        xpath_passivo_ativo='/html/body/main/div[2]/div/div[8]/div[2]/div/div[2]/div/div[5]/div/div/strong'  
        value=self.driver.find_element(By.XPATH, xpath_passivo_ativo).text
        return self.format_data_number(value)
    

    def get_liq_recorrente(self):
        xpath_liq_recorrente='/html/body/main/div[2]/div/div[8]/div[2]/div/div[2]/div/div[6]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_liq_recorrente).text
        return self.format_data_number(value)


    # Indicadores de eficiência
    def get_margem_bruta(self):
        xpath_margem_bruta='/html/body/main/div[2]/div/div[8]/div[2]/div/div[3]/div/div[1]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_margem_bruta).text
        return self.format_data_number(value)


    def get_margem_ebitda(self):
        xpath_margem_ebitda='/html/body/main/div[2]/div/div[8]/div[2]/div/div[3]/div/div[2]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_margem_ebitda).text
        return self.format_data_number(value)
    

    def get_margem_ebit(self):
        xpath_margem_ebit='/html/body/main/div[2]/div/div[8]/div[2]/div/div[3]/div/div[3]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_margem_ebit).text
        return self.format_data_number(value)


    def get_margem_liq(self):
        xpath_margem_liq='/html/body/main/div[2]/div/div[8]/div[2]/div/div[3]/div/div[4]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_margem_liq).text
        return self.format_data_number(value)


    # Indicadores de rentabilidade
    def get_roe(self):
        xpath_roe='/html/body/main/div[2]/div/div[8]/div[2]/div/div[4]/div/div[1]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_roe).text
        return self.format_data_number(value)
    

    def get_roa(self):
        xpath_roa='/html/body/main/div[2]/div/div[8]/div[2]/div/div[4]/div/div[2]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_roa).text
        return self.format_data_number(value)


    def get_roic(self):
        xpath_roic='/html/body/main/div[2]/div/div[8]/div[2]/div/div[4]/div/div[3]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_roic).text
        return self.format_data_number(value)
    

    def get_giro_ativo(self):
        xpath_giro_atio='/html/body/main/div[2]/div/div[8]/div[2]/div/div[4]/div/div[4]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xpath_giro_atio).text
        return self.format_data_number(value)
    

    # Indicadores de crescimento
    def get_cagr_receita_5_anos(self):
        xapth_cagr='/html/body/main/div[2]/div/div[8]/div[2]/div/div[5]/div/div[1]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xapth_cagr).text
        return self.format_data_number(value)
    

    def get_cagr_lucro_5_anos(self):
        xapth_cagr='/html/body/main/div[2]/div/div[8]/div[2]/div/div[5]/div/div[2]/div/div/strong'
        value=self.driver.find_element(By.XPATH, xapth_cagr).text
        return self.format_data_number(value)


    # Montar estrutura de indicadores
    def get_ind_valuation(self):
        return {
            "ind_valuation" : {
                "dividend_yield" : self.get_dividend_yield(),
                "pl" : self.get_pl(),
                "peg_ratio" : self.get_peg_ratio(),
                "p_vp" : self.get_pvp(),
                "ev_ebitda" : self.get_ev_ebitda(),
                "ev_ebit" : self.get_ev_ebit(),
                "p_ebitda" : self.get_p_ebitda(),
                "p_ebit" : self.get_p_ebit(),
                "vpa" : self.get_vpa(),
                "p_ativo" : self.get_p_ativo(),
                "lpa" : self.get_lpa(),
                "p_sr" : self.get_p_sr(),
                "p_cap_giro" : self.get_p_cap_giro(),
                "p_ativo_circ_liq" : self.get_p_ativo_circ_liq()
            }
        }


    def get_ind_debt(self):
        return {
            "ind_endividamento" : {
                "div_liq_patri_liq" : self.get_div_liq_pl(),
                "div_liq_ebitda" : self.get_div_liq_ebitda(),
                "div_liq_ebit" : self.get_div_liq_ebit(),
                "patri_liq_ativos" : self.get_patri_liq_ativos(),
                "passivos_ativos" : self.get_passivo_ativo(),
                "liq_recorrente" : self.get_liq_recorrente()
            }
        }


    def get_ind_efficiency(self):
        return {
            "ind_eficiencia" : {
                "margem_bruta" : self.get_margem_bruta(),
                "margem_ebitda" : self.get_margem_ebitda(),
                "margem_ebit" : self.get_margem_ebit(),
                "margem_liquida" : self.get_margem_liq()
            }
        }


    def get_ind_profitability(self):
        return {
            "ind_rentabilidade" : {
                "roe" : self.get_roe(),
                "roa" : self.get_roa(),
                "roic" : self.get_roic(),
                "giro_ativo" : self.get_giro_ativo()
            }
        }


    def get_ind_growth(self):
        return {
            "ind_crescimento":{
                "cagr_receita": self.get_cagr_receita_5_anos(),
                "cagr_lucro" : self.get_cagr_lucro_5_anos()
                }
            }


    # Montar estrutra final da ação
    def get_acao(self, codigo):
        return { datetime.now().strftime("%Y-%m-%d %H:%M") : {
                "name" : self.get_name(),
                "code" : codigo,
                "price" : self.get_currently_price(),
                "ind_valuation" : self.get_ind_valuation(),
                "ind_debt" : self.get_ind_debt(),
                "ind_efficiency" : self.get_ind_efficiency(),
                "ind_profitability" : self.get_ind_profitability(),
                "ind_growth" : self.get_ind_growth()

            }
        }

# Feche o navegador
test = Scraper()
print(json.dumps(test.get_acao('WEGE3'), indent=4, ensure_ascii=False))

