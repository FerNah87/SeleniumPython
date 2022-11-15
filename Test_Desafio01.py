import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#driver = webdriver.Chrome(executable_path="C:\SeleniumDrivers\chromedriver.exe")
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox(executable_path="C:\SeleniumDrivers\geckodriver.exe")
t=2

driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()
time.sleep(t)

driver.find_element_by_xpath("//input[contains(@name,'first_name')]").send_keys("Fer" + Keys.TAB + "Zal" + Keys.TAB + "cualq@cualq.com")
driver.find_element_by_xpath("//input[contains(@name,'phone')]").send_keys("1234567890" + Keys.TAB + "Fake Street" + Keys.TAB + "Fake City")
estado=Select(driver.find_element_by_xpath("//select[contains(@name,'state')]"))
estado.select_by_index(5)
driver.find_element_by_xpath("//input[contains(@name,'zip')]").send_keys("14650" + Keys.TAB + "www.google.com.ar")
driver.find_element_by_xpath("//input[contains(@value,'no')]").click()
driver.find_element_by_xpath("//textarea[contains(@class,'form-control')]").send_keys("Prueba del Desafio" + Keys.TAB + Keys.ENTER)

'''
Dos formas mas de tirar el SEND
driver.find_element_by_xpath("//button[@type='submit'][contains(.,'Send')]").click()
try:
    Send=WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit'][contains(.,'Send')]")))
    Send=driver.find_element_by_xpath("//button[@type='submit'][contains(.,'Send')]")
    ir=driver.execute_script("arguments[0].scrollIntoView();", Send)
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no estaaaaa")
'''
time.sleep(t)
driver.close()

print("La pagina de Desafio es https://demo.seleniumeasy.com/input-form-demo.html y todo OK!!!")


'''
#Nueva forma de SCROLL sin saber el tiempo (eliminar windows.scrollTo)
try:
    Buscar=WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Descubre más')]")))
    Buscar=driver.find_element_by_xpath("//span[contains(.,'Descubre más')]")
    ir=driver.execute_script("arguments[0].scrollIntoView();", Buscar)
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no estaaaaa")
'''