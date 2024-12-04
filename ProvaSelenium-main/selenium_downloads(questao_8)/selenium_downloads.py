from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configuração do WebDriver para o Chrome
driver = webdriver.Chrome()  # Certifique-se de que o chromedriver está no PATH

try:
    # Passo 1: Abrir o navegador e acessar https://www.selenium.dev/
    driver.get("https://www.selenium.dev/")
    
    # Passo 2: Navegar até a seção Downloads clicando no link correspondente
    download_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Downloads")  # Localiza o link de Downloads
    download_link.click()  # Clica no link
    
    # Esperar alguns segundos para a página carregar
    time.sleep(2)

    # Passo 3: Extrair o texto do cabeçalho principal (h1 ou h2) da página
    header = driver.find_element(By.TAG_NAME, "h1")  # Encontra o cabeçalho h1
    print(header.text)  # Imprime o texto do cabeçalho no console

finally:
    # Fechar o navegador
    driver.quit()
