from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#viejo
#driver = webdriver.Chrome(executable_path="C:\SeleniumDrivers\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\SeleniumDrivers\geckodriver.exe")

#nuevo
#driver = webdriver.Chrome()
driver = webdriver.Firefox()
#driver.get('http://selenium.dev/')


driver.get("https://demoqa.com/text-box")

print(driver.title)

driver.close()