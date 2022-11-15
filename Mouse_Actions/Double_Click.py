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

t = 3

class base_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\SeleniumDrivers\chromedriver.exe")
        # self.driver = webdriver.Firefox(executable_path="C:\SeleniumDrivers\geckodriver.exe")
        self.driver.maximize_window()

    # Mouse doble Click Seccion 24.106
    def test1(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://demoqa.com/buttons", t)
        '''
        doble = driver.find_element_by_id("doubleClickBtn")
        act = ActionChains(driver)
        act.double_click(doble).perform()
        Se crea una funcion click doble
        '''
        f.Click_Doble("xpath", "//button[contains(@id,'doubleClickBtn')]", t)

    def tearDown(self):
        driver = self.driver
        driver.close()