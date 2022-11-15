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
class base_test(unittest.TestCase):
    def setUp(self):
        # driver = webdriver.Chrome(executable_path="C:\SeleniumDrivers\chromedriver.exe")
        self.driver = webdriver.Firefox(executable_path="C:\SeleniumDrivers\geckodriver.exe")
        driver=self.driver


    def test1(self):
        driver = self.driver
        driver.get("https://demoqa.com/text-box")
        time.sleep(4)

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__== '__main__':
    unittest.main()