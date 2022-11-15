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

    #Seccion 24.112
    def test1(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://demoqa.com/automation-practice-form", t)

        f.Text_Mixto("xpath", "//input[contains(@id,'firstName')]", "Fer", 1)

        act = ActionChains(driver)
        act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        time.sleep(2)
        act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
        act.send_keys(Keys.TAB)
        act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        time.sleep(2)
        act.send_keys(Keys.TAB)

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__== '__main__':
    unittest.main()