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

driver.get("https://pixabay.com/es/")
driver.maximize_window()
time.sleep(t)


#Nueva forma de SCROLL sin saber el tiempo (eliminar windows.scrollTo)
try:
    Buscar=WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Descubre más')]")))
    Buscar=driver.find_element_by_xpath("//span[contains(.,'Descubre más')]")
    ir=driver.execute_script("arguments[0].scrollIntoView();", Buscar)
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no estaaaaa")

#driver.execute_script("window.scrollTo(0,300)")

time.sleep(t)
driver.close()

print("La pagina de EJEMPLO Scroll es https://pixabay.com/es/ y todo OK!!!")