import time
from selenium.webdriver.common.by import By

class InternetRadioPage:
    url = "https://www.internet-radio.com/"
    timeout = 3
    input_search = "//input[@name='radio']"
    btn_search = "//button[@class='btn btn-default']"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(self.timeout)

    def search_station(self, station_name):
        self.driver.find_element(By.XPATH, self.input_search).send_keys(station_name)
        self.driver.find_element(By.XPATH, self.btn_search).click()
        time.sleep(self.timeout)

    def get_current_url(self):
        return self.driver.current_url
