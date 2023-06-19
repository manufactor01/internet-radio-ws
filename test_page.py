from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
from selenium.webdriver.common.by import By
import time

service_object = Service(binary_path)
driver = webdriver.Chrome(service=service_object)

print("Cargando pagina...")
driver.get("https://betest01.bancosantafe.com/loginStep1")
driver.maximize_window()
time.sleep(10)

input_username = driver.find_element(By.ID, "username")
input_username.send_keys("username")
time.sleep(5)

btn_continuar = driver.find_element(By.ID, "global.continue")
btn_continuar.click()
time.sleep(5)

input_password = driver.find_element(By.ID, "password")
input_password.send_keys("password")
time.sleep(5)

btn_ingresar = driver.find_element(By.ID, "global.getInto")
btn_ingresar.click()

time.sleep(5)
driver.close()
