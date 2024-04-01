import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#driver = webdriver.Chrome(executable_path="C:\SeleniumDrivers\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\SeleniumDrivers\geckodriver.exe")
driver = webdriver.Chrome()
#driver = webdriver.Firefox()

t=2

driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()
time.sleep(t)

btn_send=driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Send')]")
btn_send.click()
time.sleep(t)

nombre_valid=driver.find_element(By.XPATH, "//small[@class='help-block'][contains(.,'Please supply your first name')]")
name=nombre_valid.text
#print("el valor del error es: " + name)
if(name=="Please supply your first name"):
    nombre=driver.find_element(By.XPATH, "//input[contains(@name,'first_name')]")
    nombre.send_keys("Fer")
    time.sleep(t)
    print("Nombre correcto")
else:
    print("Falta el nombre")

apellido_valid=driver.find_element(By.XPATH, "//small[@class='help-block'][contains(.,'Please supply your last name')]")
apellido=apellido_valid.text
if(apellido=="Please supply your last name"):
    apellido=driver.find_element(By.XPATH, "//input[contains(@name,'last_name')]")
    apellido.send_keys("Zal")
    time.sleep(t)
    print("Apellido correcto")
else:
    print("Falta el Apellido")

email_valid=driver.find_element(By.XPATH, "//small[@class='help-block'][contains(.,'Please supply your email address')]")
email=email_valid.text
if(email=="Please supply your email address"):
    email=driver.find_element(By.XPATH, "//input[contains(@name,'email')]")
    email.send_keys("coso@coso.com")
    time.sleep(t)
    print("Email correcto")
else:
    print("Falta Email")

print(btn_send.is_enabled())
if(btn_send.is_enabled()==False):
    print("Faltan campos por completar")
else:
    print("Todo Ok")

driver.close()

print("El Ejemplo de Validar Texto es https://demo.seleniumeasy.com/input-form-demo.html todo OK!!!")