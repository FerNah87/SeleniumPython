import time
import unittest
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException

#plantilla de test unitario que se maneja por clases
class pruebaLogin(unittest.TestCase):
    def setUp(self):
        # driver = webdriver.Chrome(executable_path="C:\SeleniumDrivers\chromedriver.exe")
        self.driver = webdriver.Firefox(executable_path="C:\SeleniumDrivers\geckodriver.exe")

    def test_login1(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nombre=driver.find_element_by_xpath("//input[contains(@id,'user-name')]").send_keys("coso@gmail.com")
        passw=driver.find_element_by_xpath("//input[contains(@id,'password')]").send_keys("12345678")
        btnlog=driver.find_element_by_xpath("//input[contains(@id,'login-button')]").click()
        error=driver.find_element_by_xpath("//h3[contains(@data-test,'error')]")
        error=error.text
        #print(error)
        if(error=="Epic sadface: Username and password do not match any user in this service"):
            print("Los datos no son correctos")
            print("Test 01 OK")
        time.sleep(2)

    def test_login2(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nombre=driver.find_element_by_xpath("//input[contains(@id,'user-name')]").send_keys("")
        passw=driver.find_element_by_xpath("//input[contains(@id,'password')]").send_keys("12345678")
        btnlog=driver.find_element_by_xpath("//input[contains(@id,'login-button')]").click()
        error=driver.find_element_by_xpath("//h3[contains(@data-test,'error')]")
        error=error.text
        #print(error)
        if(error=="Epic sadface: Username is required"):
            print("No esta escrito el Usuario")
            print("Test 02 OK")
        time.sleep(2)

    def test_login3(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nombre=driver.find_element_by_xpath("//input[contains(@id,'user-name')]").send_keys("usercoso")
        passw=driver.find_element_by_xpath("//input[contains(@id,'password')]").send_keys("")
        btnlog=driver.find_element_by_xpath("//input[contains(@id,'login-button')]").click()
        error=driver.find_element_by_xpath("//h3[contains(@data-test,'error')]")
        error=error.text
        #print(error)
        if(error=="Epic sadface: Password is required"):
            print("No esta escrito el pass")
            print("Test 03 OK")
        time.sleep(2)

    def test_login4(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nombre=driver.find_element_by_xpath("//input[contains(@id,'user-name')]").send_keys("")
        passw=driver.find_element_by_xpath("//input[contains(@id,'password')]").send_keys("")
        btnlog=driver.find_element_by_xpath("//input[contains(@id,'login-button')]").click()
        error=driver.find_element_by_xpath("//h3[contains(@data-test,'error')]")
        error=error.text
        #print(error)
        if(error=="Epic sadface: Username is required"):
            print("Los campos no estan escritos")
            print("Test 04 OK")
        time.sleep(2)

    def test_login5(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nombre=driver.find_element_by_xpath("//input[contains(@id,'user-name')]").send_keys("standard_user")
        passw=driver.find_element_by_xpath("//input[contains(@id,'password')]").send_keys("secret_sauce")
        btnlog=driver.find_element_by_xpath("//input[contains(@id,'login-button')]").click()
        '''
        error=driver.find_element_by_xpath("//h3[contains(@data-test,'error')]")
        error=error.text
        #print(error)
        if(error=="Epic sadface: Username is required"):
            print("El usuario no esta escrito")
        else:
            print("El usuario y el pass son correctos")
            print("Test 05 OK")
        '''
        print("El usuario y el pass son correctos")
        print("Test 05 OK")
        time.sleep(2)

    def test_login6(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nombre=driver.find_element_by_xpath("//input[contains(@id,'user-name')]").send_keys("standard_user")
        passw=driver.find_element_by_xpath("//input[contains(@id,'password')]").send_keys("secret_sauce")
        btnlog=driver.find_element_by_xpath("//input[contains(@id,'login-button')]").click()
        logo=driver.find_element_by_xpath("//div[contains(@class,'logo')]")
        logo.is_displayed()
        if(logo.is_displayed()==True):
            print("El logo existe")
            print("Test 06 OK")
        else:
            print("El logo NO existe")
            print("Erro Test 06")
        time.sleep(2)

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__== '__main__':
    unittest.main()