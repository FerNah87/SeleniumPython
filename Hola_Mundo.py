from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome(executable_path="C:\SeleniumDrivers\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\SeleniumDrivers\geckodriver.exe")

driver.get("https://demoqa.com/text-box")

print(driver.title)

driver.close()