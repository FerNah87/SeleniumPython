import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

class PruebaLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Firefox()
        t = 2

    def test_login1(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nom=driver.find_element("xpath", "//input[contains(@id,'user-name')]")
        clave=driver.find_element("xpath", "//input[contains(@id,'password')]")
        bt=driver.find_element("xpath", "//input[contains(@id,'login-button')]")
        nom.send_keys("rodrigo")
        clave.send_keys("admin123")
        bt.click()
        error=driver.find_element("xpath", "//h3[contains(@data-test,'error')]")
        error=error.text
        #print(error)
        if(error=="Epic sadface: Username and password do not match any user in this service"):
            print("El error de los datos es correcto")
            print("Prueba uno Ok")
        time.sleep(3)

    def test_login2(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nom=driver.find_element("xpath", "//input[contains(@id,'user-name')]")
        clave=driver.find_element("xpath", "//input[contains(@id,'password')]")
        bt=driver.find_element("xpath", "//input[contains(@id,'login-button')]")
        nom.send_keys("")
        clave.send_keys("admin123")
        bt.click()
        error=driver.find_element("xpath", "//h3[contains(@data-test,'error')]")
        error=error.text
        print(error)

        if(error=="Epic sadface: Username is required"):
            print("Falta el nombre")
            print("Prueba dos Ok")

        time.sleep(3)

    def test_login3(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nom=driver.find_element("xpath", "//input[contains(@id,'user-name')]")
        clave=driver.find_element("xpath", "//input[contains(@id,'password')]")
        bt=driver.find_element("xpath", "//input[contains(@id,'login-button')]")
        nom.send_keys("rodrigo")
        clave.send_keys("")
        bt.click()
        error=driver.find_element("xpath", "//h3[contains(@data-test,'error')]")
        error=error.text
        print(error)

        if(error=="Epic sadface: Password is required"):
            print("Falta el Password")
            print("Prueba tres Ok")

        time.sleep(3)

    def test_login4(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nom = driver.find_element("xpath", "//input[contains(@id,'user-name')]")
        clave = driver.find_element("xpath", "//input[contains(@id,'password')]")
        bt = driver.find_element("xpath", "//input[contains(@id,'login-button')]")
        nom.send_keys("")
        clave.send_keys("")
        bt.click()
        error = driver.find_element("xpath", "//h3[contains(@data-test,'error')]")
        error = error.text
        print(error)

        if (error == "Epic sadface: Username is required"):
            print("Faltan los dos campos")
            print("Prueba cuatro pendiente")

        time.sleep(3)

    def test_login5(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nom = driver.find_element("xpath", "//input[contains(@id,'user-name')]")
        clave = driver.find_element("xpath", "//input[contains(@id,'password')]")
        bt = driver.find_element("xpath", "//input[contains(@id,'login-button')]")
        nom.send_keys("standard_user")
        clave.send_keys("secret_sauce")
        bt.click()

        elemento = driver.find_element("xpath", "//div[contains(@class,'app_logo')]")
        elemento.is_enabled()
        #elemento.is_displayed()
        #elemento=elemento.text
        print("El elemento es: "+str(elemento))

        time.sleep(3)

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()
    
# Nota
# Se reemplaza el find_element por find_element y "xpath" 
# Se genera la base (setUp tearDown) y los import
# Se crea la funcion para cada prueba (login1 2 3 ...) 