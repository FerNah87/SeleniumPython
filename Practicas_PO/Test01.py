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
from Funciones.Page_Login import Pagina_Login

#Tiempo Globlal
tg = 4
# plantilla de test unitario que se maneja por clases
class base_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\SeleniumDrivers\chromedriver.exe")
        # self.driver = webdriver.Firefox(executable_path="C:\SeleniumDrivers\geckodriver.exe")

    # Crear una funcion de Saludo Seccion 20.74
    # def test1(self):
    #     driver = self.driver
    #     f = Funciones_Globales()
    #     f.saludos()
    #     f.saludos2()

    # funcion que nos regrese un valor/resultado
    # def test1(self):
    #     driver = self.driver
    #     f = Funciones_Globales(driver)
    #     f.Navegar("https://www.saucedemo.com/", tg)

    # Funcion de Texto con Xpath
    # def test1(self):
    #     driver = self.driver
    #     f = Funciones_Globales(driver)
    #     f.Navegar("https://www.saucedemo.com/", tg)
    #     f.Text_Xpath("//input[contains(@id,'user-name')]", "Fernando", tg)
    #     f.Text_Xpath("//input[contains(@id,'password')]", "admin123", tg)

    #Mejora de Xpath (validar)
    # def test1(self):
    #     driver = self.driver
    #     f = Funciones_Globales(driver)
    #     f.Navegar("https://www.saucedemo.com/", tg)
    #     f.Text_Xpath_Validar("//input[contains(@id,'user-name')]", "Fernando", tg)
    #     f.Text_Xpath_Validar("//input[contains(@id,'password')]", "admin123", tg)
    #     f.Click_Xpath_Validar("//input[contains(@id,'login-button')]", tg)

    # Funcion de Texto con ID
    # def test1(self):
    #     driver = self.driver
    #     f = Funciones_Globales(driver)
    #     f.Navegar("https://www.saucedemo.com/", tg)
    #     f.Text_Id("user-name", "fernando", tg)
    #     f.Text_Id("password", "admin123", tg)

    # Mejora de ID (validar).
    # def test1(self):
    #     driver = self.driver
    #     f = Funciones_Globales(driver)
    #     f.Navegar("https://www.saucedemo.com/", tg)
    #     f.Text_Id_Validar("user-name", "fernando", tg)
    #     f.Text_Id_Validar("password", "admin123", tg)
    #     f.Click_Id_Validar("login-button", tg)

    #Seccion 20.82
    # def test1(self):
    #     driver = self.driver
    #     f=Funciones_Globales(driver)
    #     pg= Pagina_Login(driver)
    #     pg.Loguin_Master("https://www.saucedemo.com/", "Fernando", "admin", tg)

    #Seccion 20.82
    def test1(self):
        driver = self.driver
        f=Funciones_Globales(driver)
        f.Navegar("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html", tg)
        f.Select_Xpath_Text("//select[contains(@id,'select-demo')]", "Sunday", tg)
        #Tipo texto
        #f.Select_Xpath_Type("//select[contains(@id,'select-demo')]", "texto", "Sunday", tg)
        #Tipo Value
        #f.Select_Xpath_Type("//select[contains(@id,'select-demo')]", "value", "Friday", tg)
        #Tipo Index
        #f.Select_Xpath_Type("//select[contains(@id,'select-demo')]", "index", "3", tg)
        #Upload Imagen
        #f.Navegar("https://testpages.herokuapp.com/styled/file-upload-test.html", tg)
        #f.Upload_Xpath("//input[contains(@id,'fileinput')]", "C://Users//Fer - Patagonia//Python//SeleniumPython//Imagenes//demo01.jpg", tg)
        #f.Upload_Id("fileinput", "C://Users//Fer - Patagonia//Python//SeleniumPython//Imagenes//demo01.jpg", tg)
        #Check
        # f.Navegar("https://demo.seleniumeasy.com/basic-checkbox-demo.html", tg)
        # f.Check_Xpath("//input[contains(@id,'isAgeSelected')]", tg)
        #f.Check_Id("isAgeSelected", tg)

    #Seccion 20.88 Reto MultiCheck
    # def testReto(self):
    #     driver = self.driver
    #     f=Funciones_Globales(driver)
    #     f.Navegar("https://demo.seleniumeasy.com/basic-checkbox-demo.html", tg)
    #     for multiple in range(2,6):
    #         f.Multi_Check_Xpath(tg, "(//input[@type='checkbox'])["+str(multiple)+"]")

        f.Salida()



