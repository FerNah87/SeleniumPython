import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from ...Funciones.Funciones import Funciones_Globales
from selenium.webdriver import ActionChains

t=2

class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        # driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
        self.driver.maximize_window()



    def test1(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://demoqa.com/automation-practice-form",t)

        f.Texto_Mixto("id","firstName","Rodrigo")
        f.Texto_Mixto("id","lastName","Perez")
        f.Texto_Mixto("id","userEmail","rodrigo@gmail.com")
        f.Click_Mixto("xpath","//label[@for='gender-radio-1'][contains(.,'Male')]")
        f.Texto_Mixto("id","userNumber","5546454345")

        f.Click_Mixto("xpath","//input[contains(@id,'dateOfBirthInput')]",4)
        f.Click_Mixto("xpath","//div[contains(@aria-label,'Choose Tuesday, August 24th, 2021')]",2).send_keys(Keys.TAB).send_keys("Demo del texto")









        time.sleep(4)




    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()






