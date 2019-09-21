from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from time import sleep
import conect_what
import json
# number_user = "saulo oliveira" # +55 92 9120-9256 # +55 92 9120-9256 
binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

# Criar instância do navegador
browser = webdriver.Firefox(firefox_binary=binary, executable_path=r"C:\\geckodriver.exe")

with open("json/phones.json") as file:
    data = json.load(file)

labels = []

for intent in data["intents"]:
    # for number_user in intent["phone"]:
    if intent["phone"] not in labels:
        labels.append(intent["phone"])
    print('[Lepros] ---> Lista de telefone:')
    # print(labels[0])

# Selenium irá entrar no whats e aguardar 10 segundos até o dom estiver pronto.
browser.get('https://web.whatsapp.com')
print('[Lepros] ---> inicializando o bot')
sleep(10)

def mesage(mesage_bot) :
    conversa_user = browser.find_element_by_class_name('X7YrQ')
    conversa_user.click()
    enviar_texto = browser.find_element_by_class_name('_3u328')
    enviar_texto.send_keys(mesage_bot)
    enviar_texto.send_keys(Keys.ENTER)
    sleep(5)

while True:
    #Selecionamos o elemento da caixa de pesquisa do whats pela classe.
    caixa_de_pesquisa = browser.find_element_by_class_name('_2zCfw')
    #Escreveremos o nome do contato na caixa de pesquisa e aguardaremos 2 segundos.
    caixa_de_pesquisa.send_keys(labels[0])
    sleep(2)
    mesage("Sou o bot Mané e meu criador desejamos a você um ótimo final de semana :)")
    
    

    

    


























 

 
