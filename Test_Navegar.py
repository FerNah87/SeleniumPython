import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(executable_path="C:\SeleniumDrivers\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\SeleniumDrivers\geckodriver.exe")
driver = webdriver.Chrome()
#driver = webdriver.Firefox()

t=2

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(t)

driver.get("https://www.google.com/")
time.sleep(t)

driver.get("https://www.youtube.com/")
time.sleep(t)

driver.execute_script("window.history.go(-1)")
#driver.back()
time.sleep(t)

driver.execute_script("window.history.go(-1)")
#driver.back()
time.sleep(t)

driver.close()

print("Exito Navegar!!!")
#Se puede navegar por diferentes paginas