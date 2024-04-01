import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from ..Funciones.Funciones import Funciones_Globales
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

t=2

class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        #self.driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
        self.driver.maximize_window()



    def test1(self):
        driver = self.driver
        driver.implicitly_wait(5)
        f = Funciones_Globales(driver)
        f.Navegar("https://www.google.com.mx/?hl=es-419",t)

        driver.execute_script(" var a = prompt('cual es tu nombre: ')")
        time.sleep(5)











    def tearDown(self):
        driver = self.driver
        #driver.close()

if __name__ == '__main__':
    unittest.main()






