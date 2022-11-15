import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(executable_path="C:\SeleniumDrivers\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\SeleniumDrivers\geckodriver.exe")

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)

nom=driver.find_element(By.ID, "userName")
nom.send_keys("Fernando")
time.sleep(2)
email=driver.find_element(By.ID, "userEmail")
email.send_keys("coso@coso.com")
time.sleep(2)
#es la otra forma
driver.find_element(By.ID, "currentAddress").send_keys("Hurlingham")
time.sleep(2)
driver.find_element(By.ID, "permanentAddress").send_keys("Villa Tesei")
time.sleep(2)

#para bajar la ventana y que se vea el boton y no de error
driver.execute_script("window.scrollTo(0,300)")
time.sleep(2)

driver.find_element(By.ID, "submit").click()
time.sleep(2)

driver.close()

print("Exito Selector By_Id!!!")