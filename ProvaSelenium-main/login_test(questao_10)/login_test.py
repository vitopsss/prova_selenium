from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configuração do WebDriver para o Chrome
driver = webdriver.Chrome()  # Certifique-se de que o chromedriver está no PATH

try:
    # Passo 1: Acessar o site https://the-internet.herokuapp.com/login
    driver.get("https://the-internet.herokuapp.com/login")
    
    # Passo 2: Preencher o formulário de login
    username_field = driver.find_element(By.ID, "username")  # Localiza o campo de username
    password_field = driver.find_element(By.ID, "password")  # Localiza o campo de password
    
    username_field.send_keys("tomsmith")  # Preenche o campo de username
    password_field.send_keys("SuperSecretPassword!")  # Preenche o campo de password
    
    # Passo 3: Clicar no botão de login
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")  # Localiza o botão de login
    login_button.click()  # Clica no botão
    
    # Esperar alguns segundos para garantir que a página carregue
    time.sleep(2)
    
    # Passo 4: Validar se o login foi bem-sucedido
    success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")  # Localiza a mensagem de sucesso
    
    # Verifica se a mensagem contém o texto esperado
    if "You logged into a secure area!" in success_message.text:
        print("Login bem-sucedido!")
    else:
        print("Login falhou.")
    
finally:
    # Fechar o navegador
    driver.quit()
