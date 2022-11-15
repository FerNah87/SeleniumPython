#arrastrar y soltar
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

class base_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\SeleniumDrivers\chromedriver.exe")
        # self.driver = webdriver.Firefox(executable_path="C:\SeleniumDrivers\geckodriver.exe")
        self.driver.maximize_window()

    def test1(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        #f.Navegar("https://demo.seleniumeasy.com/drag-and-drop-demo.html", t)
        f.Navegar("https://testpages.herokuapp.com/styled/drag-drop-javascript.html", t)
        f.Drag_and_Drop("xpath", "//div[contains(@id,'draggable1')]", "//div[contains(@id,'droppable1')]", 2)

        # f.Navegar("https://jqueryui.com/draggable/", t)
        # f.Drag_and_DropXY("id", "draggable", 150, 120, 2)

    def tearDown(self):
        driver = self.driver
        driver.close()
if __name__== '__main__':
    unittest.main()