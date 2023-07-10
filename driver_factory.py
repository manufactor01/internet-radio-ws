from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path

class DriverFactory:

    def create_chrome_driver(self):
        service_object = Service(binary_path)
        return webdriver.Chrome(service=service_object)
