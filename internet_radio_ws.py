import csv
import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
from selenium.webdriver.common.by import By

from utils import process_url
from utils import process_name

TIMEOUT = 3
URL = "https://www.internet-radio.com/"

def search_station(driver, station_name):
    input_search = driver.find_element(By.XPATH, "//input[@name='radio']")
    input_search.send_keys(station_name)
    btn_search = driver.find_element(By.XPATH, "//button[@class='btn btn-default']")
    btn_search.click()
    time.sleep(TIMEOUT)

def get_stations(driver):
    current_url = driver.current_url

    req = requests.get(current_url)
    statusCode = req.status_code
    htmlText = req.text
    html = BeautifulSoup(req.text, "html.parser")
    entradas = html.find('table', {'class': 'table table-striped'})
    elementos = entradas.find_all('tr')

    names = []
    urls = []

    for elemento in elementos:
        sub_elementos = elemento.find_all('td')

        # get titles
        titulo = process_name(sub_elementos[2].find('h4').getText())
        names.append(titulo)

        # get urls
        enlaces = sub_elementos[1].find_all('a', href=True)
        url = process_url(enlaces[1]['href'])
        urls.append(url)

    dicc = {
            'names': names,
            'urls': urls
            }

    return dicc

def search_and_get_stations(search_name, file_name):
    service_object = Service(binary_path)
    driver = webdriver.Chrome(service=service_object)

    driver.get(URL)
    driver.maximize_window()
    time.sleep(TIMEOUT)

    search_station(driver, search_name)
    dicc = get_stations(driver)

    df = pd.DataFrame(dicc)
    df.to_csv(file_name, index=False)
    driver.close()
