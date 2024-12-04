from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configuração do WebDriver para o Chrome
driver = webdriver.Chrome()

try:
    # Passo 1: Acessar uma página que gera um alerta
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    
    # Passo 2: Acionar o alerta (clicar no botão que gera o alerta)
    button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
    button.click()
    
    # Passo 3: Lidar com o alerta
    alert = driver.switch_to.alert  # Alternar para o alerta
    print(f"Texto do alerta: {alert.text}")  # Opcional: Obter o texto do alerta
    alert.accept()  # Fechar o alerta clicando em "OK"
    
    print("Alerta fechado com sucesso!")

finally:
    # Fechar o navegador
    time.sleep(2)
    driver.quit()
