import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#driver = webdriver.Chrome(executable_path="C:\SeleniumDrivers\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\SeleniumDrivers\geckodriver.exe")

driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
driver.maximize_window()
driver.implicitly_wait(5)
t=2

select_day=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[contains(@id,'select-demo')]")))
select_day=driver.find_element_by_xpath("//select[contains(@id,'select-demo')]")

#Opciones para probar el dropdown
select_day=Select(select_day)
time.sleep(t)
select_day.select_by_visible_text("Sunday")
time.sleep(t)
select_day.select_by_index(3)
time.sleep(t)
select_day.select_by_value("Saturday")
time.sleep(t)

driver.execute_script("window.scrollTo(0,300)")
time.sleep(t)

ciudad=Select(driver.find_element_by_id("multi-select"))
time.sleep(t)
ciudad.select_by_index(1)
time.sleep(t)
ciudad.select_by_index(2)
time.sleep(t)
ciudad.select_by_index(3)
time.sleep(t)
ciudad.select_by_index(4)
time.sleep(t)
ciudad.select_by_index(5)
time.sleep(t)

driver.find_element_by_xpath("//*[@id='printAll']").click()


time.sleep(t)
driver.close()

print("La pagina de EJEMPLO es  https://demo.seleniumeasy.com/basic-select-dropdown-demo.html y todo OK!!!")