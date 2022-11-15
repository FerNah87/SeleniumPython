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
from Funciones.Funciones import Funciones_Globales
from selenium.webdriver import ActionChains

t = 2
#plantilla de test unitario que se maneja por clases
class base_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\SeleniumDrivers\chromedriver.exe")
        # self.driver = webdriver.Firefox(executable_path="C:\SeleniumDrivers\geckodriver.exe")
        self.driver.maximize_window()

    #Seccion 24.104
    def test1(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://www.saucedemo.com/", t)

        # f.Text_Mixto("id", "user-name", "standard_user", t)
        # f.Text_Mixto("id", "password", "secret_sauce", t)
        # f.Click_Mixto("id", "login-button", t)

        f.Text_Mixto("xpath", "//input[contains(@id,'user-name')]", "standard_user", t)
        f.Text_Mixto("xpath", "//input[contains(@id,'password')]", "secret_sauce", t)
        f.Click_Mixto("xpath", "//input[contains(@id,'login-button')]", t)

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__== '__main__':
    unittest.main()