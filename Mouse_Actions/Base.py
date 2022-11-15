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
        #el video no esta actualizado se sigue el ejemplo escrito
        f.Navegar("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", t)

        # f.Text_Mixto("id", "txtUsername", "Admin", t)
        # f.Text_Mixto("id", "txtPassword", "admin123", t)
        # f.Click_Mixto("id", "btnLogin", t)
    #     f.Text_Mixto("xpath", "//input[@name='username']", "Admin", t)
    #     f.Text_Mixto("xpath", "//input[@name='password']", "admin123", t)
    #     f.Click_Mixto("xpath", "//button[@type='submit']", t)
    #
        admin = driver.find_element_by_id("menu_admin_viewAdminModule")
        sub1 = driver.find_element_by_id("menu_admin_UserManagement")
        sub2 = driver.find_element_by_id("menu_admin_viewSystemUsers")
    #     # admin = driver.find_element_by_xpath("(//span[contains(.,'Admin')])[1]", t)
    #     # sub1 = driver.find_element_by_xpath("(//span[contains(.,'User Management')])[2]", t)
    #     # sub2 = driver.find_element_by_xpath("//a[contains(.,'Users')]", t)
    #
    #     #con cada click abre los sumenus
        act = ActionChains(driver)
        act.move_to_element(admin).move_to_element(sub1).move_to_element(sub2).click().perform()

