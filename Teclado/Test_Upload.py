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

driver.get("https://testpages.herokuapp.com/styled/file-upload-test.html")
driver.maximize_window()
driver.implicitly_wait(5)
t=2

try:
    Buscar=WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@id,'fileinput')]")))
    Buscar=driver.find_element_by_xpath("//input[contains(@id,'fileinput')]")
    Buscar.send_keys("C://Users//Fer - Patagonia//Python//SeleniumPython//Imagenes//Screenshot 2022-10-04 114556.jpg")
    time.sleep(t)
    driver.find_element_by_xpath("//input[contains(@id,'itsanimage')]").click()
    driver.find_element_by_xpath("//input[contains(@type,'submit')]").click()
    time.sleep(t)
#VEEEEER

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no estaaaaa")

driver.execute_script("window.scrollTo(0,300)")

time.sleep(t)
driver.close()

print("La pagina de EJEMPLO UpLoad es https://testpages.herokuapp.com/styled/file-upload-test.html y todo OK!!!")