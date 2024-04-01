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

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(t)

#validar el boton
btn_submit=driver.find_element_by_xpath("//button[@type='button'][contains(.,'Submit')]")
print(btn_submit.is_enabled())

if(btn_submit.is_enabled()==True):
    print("Puede dar click")
else:
    print("No esta activo")

driver.close()

print("Validar el Boton https://demoqa.com/text-box todo OK!!!")