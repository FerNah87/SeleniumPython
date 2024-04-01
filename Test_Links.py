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

#obtener los links de la pagina
links=driver.find_elements(By.TAG_NAME, "a")

#len cuenta la cantidad de links de la pagina
print("El numero de Links de la pagina es: ", len(links))

#crea la funcion NUM. recorre en Links y guarda en la variable NUM, imprime la propiedad NUM y TEXT (nos da los nombres de los links)
for num in links:
    print(num.text)

driver.find_element(By.LINK_TEXT, "Date pickers").click()
time.sleep(t)
driver.find_element(By.LINK_TEXT, "Bootstrap Date Picker").click()
time.sleep(t)
driver.find_element(By.LINK_TEXT, "Date pickers").click()
time.sleep(t)
driver.find_element(By.LINK_TEXT, "JQuery Date Picker").click()
time.sleep(t)

time.sleep(t)
driver.close()

print("La pagina de Link es https://demo.seleniumeasy.com/input-form-demo.html y todo OK!!!")

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