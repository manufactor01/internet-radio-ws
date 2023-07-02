from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path

from internet_radio_page import InternetRadioPage
from internet_radio_crawler import InternetRadioCrawler

def search_and_get_stations(search_name, filename):
    service_object = Service(binary_path)
    driver = webdriver.Chrome(service=service_object)

    p = InternetRadioPage(driver)
    p.open()
    p.search_station(search_name)

    current_url = p.get_current_url()
    ws = InternetRadioCrawler(current_url)
    ws.generate_csv(filename)

    driver.close()
