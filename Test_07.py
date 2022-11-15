import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(executable_path="C:\SeleniumDrivers\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\SeleniumDrivers\geckodriver.exe")

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)

nom=driver.find_element_by_xpath("//input[@type='text' and @id='userName']")
nom.send_keys("Fernando")
nom.send_keys(Keys.TAB + "cualquiera@cualquiera.com" + Keys.TAB + "Hurlingham" + Keys.TAB + "Villa Tesei" + Keys.TAB + Keys.ENTER)

driver.execute_script("window.scrollTo(0,300)")
time.sleep(2)

driver.find_element_by_xpath("(//span[contains(@class,'text')])[2]").click()
time.sleep(2)

driver.close()

print("Exito Test Keys!!!")
#Con un solo Selector completar el cuestionario