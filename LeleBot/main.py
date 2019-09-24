from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from time import sleep
# import pandas as pd
import json
import requests


send_mesage = "boa tarde, já comprou nossos produtos de atacado"
name_bot = '+55 92 8828-7643'
with open("json/phones.json") as file:
    phone = json.load(file)

phones = []
json_names = []
bot_users = {}    

for intent in phone["intents"]:
    if intent["name"] not in json_names:
        json_names.append(intent["name"]) 

    if intent["phone"] not in phones:
        phones.append(intent["phone"])


# phone = phones[1]
# url_init = 'https://api.whatsapp.com/send?'
# url_phone = 'phone=' + phone
# url_text = '&text=' + send_mesage
# url = url_init + url_phone + url_text
# binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
# browser = webdriver.Firefox(firefox_binary=binary, executable_path=r"C:\\geckodriver.exe")
# browser.get(url)        


aux = 0
for phone in phones+1:
    print('[Lepros] ---> Numero da pessoa : ' + ''.join(e for e in phone if e.isalnum()) )
    phone = ''.join(e for e in phone if e.isalnum())
    if aux == 0:
        url_init = 'https://api.whatsapp.com/send?'
        url_phone = 'phone=' + phone
        url_text = '&text=' + send_mesage
        url = url_init + url_phone + url_text
        binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        browser = webdriver.Firefox(firefox_binary=binary, executable_path=r"C:\\geckodriver.exe")
        browser.get(url) 
        browser.find_element_by_id("action-button").click()
        sleep(3)
        browser.find_element_by_class_name('action__link').click()
        sleep(10)
        text_box = browser.find_element_by_class_name('_3u328')
        text_box.send_keys(Keys.ENTER)
        aux = 1
    else :
        search_box = browser.find_element_by_class_name('_2zCfw')
        search_box.send_keys(name_bot)



    






  







# for phone in phones:
#     print('[Lepros] ---> Numero da pessoa : ' + ''.join(e for e in phone if e.isalnum()) )
#     phone = ''.join(e for e in phone if e.isalnum())
#     url_init = 'https://api.whatsapp.com/send?'
#     url_phone = 'phone=' + phone
#     url_text = '&text=' + send_mesage
#     url = url_init + url_phone + url_text
#     binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
#     browser = webdriver.Firefox(firefox_binary=binary, executable_path=r"C:\\geckodriver.exe")
#     browser.get(url)
#     browser.find_element_by_id("action-button").click()
#     sleep(3)
#     browser.find_element_by_class_name('action__link').click()
#     sleep(10)
#     text_box = browser.find_element_by_class_name('_3u328')
#     text_box.send_keys(Keys.ENTER)

        



        






# # phone = "559284511344" #Eric
# # +55 92 8451-1344

# phone = "559281274631" #Daniel
# # +55 92 8127-4631

# # https://api.whatsapp.com/send?phone=559284511344&text=oi
# url_init = 'https://api.whatsapp.com/send?'
# url_phone = 'phone=' + phone
# url_text = '&text=' + send_mesage



# url = url_init + url_phone + url_text
# binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
# browser = webdriver.Firefox(firefox_binary=binary, executable_path=r"C:\\geckodriver.exe")
# browser.get(url)


# browser.find_element_by_id("action-button").click()
# sleep(3)
# browser.find_element_by_class_name('action__link').click()
# sleep(10)
# text_box = browser.find_element_by_class_name('_3u328')
# text_box.send_keys(Keys.ENTER)

