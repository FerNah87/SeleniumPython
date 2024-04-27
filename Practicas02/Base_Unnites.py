import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox
        # self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe") esto es la forma vieja
        # driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
        t = 2

    def test1(self):
        driver = self.driver
        driver.get("") #al correrlo asi tira error, se tiene que insertar la web
        driver.maximize_window()
        time.sleep(2)
        
    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()
    
# Unittest: nos da la funcionalidad de crear pruebas mas eficientes, mas ordenada, se crea la carpeta y archivo (se importa las libreriras correspondientes), 
# 	se crea la plantilla con una CLASE (class base_Test)
# 	Se crean 2 funciones clases 
# 		de apertura - setup(self) *con su argumento
# 		de clausura - tearDown(self) *con su argumento
# 	Se crea entre la apertura y clausura la funcion para testear (test1)
