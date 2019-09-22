from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from time import sleep
import conect_what
import json
from bs4 import BeautifulSoup
import requests

url = 'https://web.whatsapp.com'
soup = BeautifulSoup(requests.get(url).content, 'html.parser')

binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

# Criar instância do navegador
browser = webdriver.Firefox(firefox_binary=binary, executable_path=r"C:\\geckodriver.exe")

with open("json/phones.json") as file:
    data = json.load(file)

labels = []
json_names = []
bot_users = {}

for intent in data["intents"]:
    if intent["name"] not in json_names:
        json_names.append(intent["name"]) 

    if intent["phone"] not in labels:
        labels.append(intent["phone"]) 

# Selenium irá entrar no whats e aguardar 10 segundos até o dom estiver pronto.
browser.get(url)
sleep(10)

def send_mesage(name, response) :

    search_box = browser.find_element_by_class_name('_2zCfw')
    search_box.send_keys(name)
    print('[Lepros] ---> nome do contato vindo do json: ' + name)
    sleep(2)
    contact_box = browser.find_element_by_class_name('X7YrQ')
    contact_name  = browser.find_element_by_class_name("_19RFN").text
    # message = browser.find_elements_by_class_name("vW7d1")[-1]
	# images = message.find_elements_by_class_name("_3v3PK")
    print('[Lepros] ---> nome do contato : ' + contact_name )

    if name not in bot_users:
        if contact_name == name:
            bot_users[contact_name] = True
            contact_box.click()
            text_box = browser.find_element_by_class_name('_3u328')
            text_box.send_keys(response + contact_name)
            text_box.send_keys(Keys.ENTER)
        else :
            browser.find_element_by_class_name('_2heX1').click()
            print('[Lepros] ---> nome do contato : ' 
                + contact_name + 
                " não é igual ao nome do contato vindo do json :" 
                + name )    
            print("não encontrou o nome")
            

for item in json_names:
    send_mesage(item, "OI sou o bot e funciona! I am alive  ")























 

 
