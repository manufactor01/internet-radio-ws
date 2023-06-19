import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
from selenium.webdriver.common.by import By
import time

def process_url(url):
    SEP = "?u="
    url_list = url.split(SEP)
    return url_list[1]

def process_name(name):
    return name.replace('\"', '')
TIMEOUT = 3

service_object = Service(binary_path)
driver = webdriver.Chrome(service=service_object)

driver.get("https://www.internet-radio.com/")
driver.maximize_window()
time.sleep(TIMEOUT)

input_search = driver.find_element(By.XPATH, "//input[@name='radio']")
input_search.send_keys("industrial")

btn_search = driver.find_element(By.XPATH, "//button[@class='btn btn-default']")
btn_search.click()
time.sleep(TIMEOUT)

current_url = driver.current_url
print(current_url)
req = requests.get(current_url)
statusCode = req.status_code
htmlText = req.text
print(htmlText)

html = BeautifulSoup(req.text, "html.parser")
entradas = html.find('table', {'class': 'table table-striped'})
elementos = entradas.find_all('tr')

names = []
urls = []

for elemento in elementos:
    sub_elementos = elemento.find_all('td')

    # obtener título
    #titulo = sub_elementos[2].find('h4')
    titulo = process_name(sub_elementos[2].find('h4').getText())
    names.append(titulo)

    # obtener enlace
    enlaces = sub_elementos[1].find_all('a', href=True)
    url = process_url(enlaces[1]['href'])
    urls.append(url)

dicc = {
        'names': names,
        'urls': urls
        }

df = pd.DataFrame(dicc)
df.to_csv('prueba.csv', index=False)
driver.close()
