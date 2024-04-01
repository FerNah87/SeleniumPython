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

driver.get("https://demo.seleniumeasy.com/bootstrap-modal-demo.html")
driver.maximize_window()
time.sleep(t)

driver.find_element(By.XPATH, "//a[@href='#myModal0']").click()
time.sleep(t)
driver.find_element(By.XPATH, "(//a[@href='#'][contains(.,'Save changes')])[1]").click()
time.sleep(t)
driver.find_element(By.XPATH, "//a[@href='#myModal0']").click()
time.sleep(t)
driver.find_element(By.XPATH, "(//a[@href='#'][contains(.,'Close')])[1]").click()
time.sleep(t)

driver.close()

print("El Ejemplo de Alert es https://demo.seleniumeasy.com/bootstrap-modal-demo.htmly todo OK!!!")