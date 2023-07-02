import time

class InternetRadioPage:
    url = "https://www.internet-radio.com/"
    timeout = 3
    input_search = "//input[@name='radio']"
    btn_search = "//button[@class='btn btn-default']"

    def __init__(self, driver):
        self.driver = driver

    def open(self, station_name):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(self.timeout)


