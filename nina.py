from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from time import sleep
 
binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
 
# Criar instância do navegador
browser = webdriver.Firefox(firefox_binary=binary, executable_path=r"C:\\geckodriver.exe")
# Selenium irá entrar no whats e aguardar 10 segundos até o dom estiver pronto.
browser.get('https://web.whatsapp.com')
print('inicializando o bot')
sleep(10)

bot_users = {}

number_users = "+55 92 88287643" # +55 92 9120-9256 # +55 92 9120-9256 


while True:
    #Selecionamos o elemento da caixa de pesquisa do whats pela classe.
    caixa_de_pesquisa = browser.find_element_by_class_name('_2zCfw')

    #Escreveremos o nome do contato na caixa de pesquisa e aguardaremos 2 segundos.
    caixa_de_pesquisa.send_keys(number_users)
    sleep(2)
    
    

    conversa_user = browser.find_element_by_class_name('X7YrQ')
    conversa_user.click()
    
    enviar_texto = browser.find_element_by_class_name('_3u328')

    enviar_texto.send_keys("Vou é um mortal então não manda em porcaria nenhuma")
    enviar_texto.send_keys(Keys.ENTER)
    sleep(5)

    


























 

 
