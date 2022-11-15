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

driver.get("https://demoqa.com/")
driver.maximize_window()
time.sleep(t)

titulo=driver.find_element_by_xpath("//img[@src='/images/Toolsqa.jpg']")
print(titulo.is_displayed())

btn1=driver.find_element_by_xpath("(//div[contains(@class,'card-up')])[1]")

if(titulo.is_displayed()==True):
    print("Existe la imagen")
    btn1.click()
    time.sleep(t)
else:
    print("No existe dicha imagen")

driver.close()

print("El Ejemplo de Alert es https://demoqa.com/ todo OK!!!")