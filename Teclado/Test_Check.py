import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

#driver = webdriver.Chrome(executable_path="C:\SeleniumDrivers\chromedriver.exe")
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox(executable_path="C:\SeleniumDrivers\geckodriver.exe")

driver.get("https://demo.seleniumeasy.com/basic-checkbox-demo.html")
driver.maximize_window()
driver.implicitly_wait(10)
t=2

btn1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type,'checkbox')])[1]")))
btn1.click()
btn2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type,'checkbox')])[2]")))
btn2.click()
btn3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type,'checkbox')])[3]")))
btn3.click()
btn4 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type,'checkbox')])[4]")))
btn4.click()
btn5 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type,'checkbox')])[5]")))
btn5.click()

#para bajar la ventana y que se vea el boton y no de error
driver.execute_script("window.scrollTo(0,300)")
time.sleep(t)

driver.find_element_by_xpath("//input[@value='Check All']").click()

time.sleep(t)
driver.close()

print("La pagina de EJEMPLO es  https://demo.seleniumeasy.com/basic-checkbox-demo.html y todo OK!!")