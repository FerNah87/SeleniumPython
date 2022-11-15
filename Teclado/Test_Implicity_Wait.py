import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome(executable_path="C:\SeleniumDrivers\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\SeleniumDrivers\geckodriver.exe")

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
#tiempo de espera a que falle algo
driver.implicitly_wait(15)

t=2
time.sleep(t)

nom=driver.find_element_by_xpath("//input[contains(@id,'userName')]")
nom.send_keys("Fernando")
time.sleep(t)
email=driver.find_element_by_xpath("//input[contains(@id,'userEmail')]")
email.send_keys("coso@coso.com")
time.sleep(t)
#es la otra forma
driver.find_element_by_xpath("//*[@id='currentAddress']").send_keys("Hurlingham")
time.sleep(t)
driver.find_element_by_xpath("//*[@id='permanentAddress']").send_keys("Villa Tesei")
time.sleep(t)

#para bajar la ventana y que se vea el boton y no de error
driver.execute_script("window.scrollTo(0,300)")
time.sleep(t)

driver.find_element_by_xpath("//*[@id='submit']").click()
time.sleep(t)

driver.close()

print("Exito Test Implicity Wait!!!")