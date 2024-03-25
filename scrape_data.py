from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Scraper():
    
    url='https://statusinvest.com.br/'
    path_list_acoes='lista_acoes.txt'
    list_acoes:list

    driver:webdriver.Chrome
    service:Service
    wait:WebDriverWait

    def __init__(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service = self.service)
        self.wait = WebDriverWait(self.driver, 10)

        self.get_url(self.url)


    def get_url(self, url):
        self.driver.get(url)


    def read_arq_acoes(self):
        with open(self.path_list_acoes, 'r') as arq_acoes:
            self.list_acoes=arq_acoes.read().split('\n')
        arq_acoes.close()

    
    def set_url_fii(self, fii):
        url_fii=self.url+'fundos-imobiliarios/'+fii
        self.get_url(url_fii)


    def set_url_fiagro(self, fiagro):
        url_fiagro=self.url+'fiagros/'+fiagro
        self.get_url(url_fiagro)


    def set_url_acao(self, acao):
        url_acao=self.url+'acoes/'+acao
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




        
'''x = Scraper()
acao='BBSE3'

x.set_url_acao(acao)

print(x.get_currently_price())
print(x.get_dividend_yield())
print(x.get_pl())
print(x.get_peg_ratio())
print(x.get_pvp())
print(x.get_ev_ebitda())
print(x.get_ev_ebit())
print(x.get_p_ebitda())
print(x.get_p_ebit())
print(x.get_vpa())
print(x.get_p_ativo())
print(x.get_lpa())
print(x.get_p_sr())
print(x.get_p_cap_giro())
print(x.get_p_ativo_circ_liq())
'''

