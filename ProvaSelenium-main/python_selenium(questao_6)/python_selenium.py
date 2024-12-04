from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configuração do WebDriver para o Chrome
driver = webdriver.Chrome()  # Certifique-se de que o chromedriver está no PATH

try:
    # Passo 1: Abrir o navegador e acessar o site do Google
    driver.get("https://www.google.com")
    
    # Passo 2: Encontrar a barra de pesquisa
    search_bar = driver.find_element(By.NAME, "q")  # 'q' é o nome do elemento de pesquisa no Google

    # Passo 3: Digitar "Python Selenium" e pressionar Enter
    search_bar.send_keys("Python Selenium")
    search_bar.send_keys(Keys.RETURN)

    # Esperar alguns segundos para carregar os resultados
    time.sleep(2)

    # Passo 4: Fazer a captura de tela da página de resultados
    driver.save_screenshot("resultado.png")

finally:
    # Fechar o navegador
    driver.quit()
