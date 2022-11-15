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

#Creando funciones
class Pagina_Login():

    #con esta funcion se inicializan las variables
    def __init__(self, driver):
        self.driver = driver

    # def Loguin_Master(self, t):
    #     driver = self.driver
    #     f = Funciones_Globales(driver)
    #     f.Navegar("https://www.saucedemo.com/", t)
    #     f.Text_Xpath_Validar("//input[contains(@id,'user-name')]", "Fernando", t)
    #     f.Text_Xpath_Validar("//input[contains(@id,'password')]", "admin123", t)
    #     f.Click_Xpath_Validar("//input[contains(@id,'login-button')]", t)

    #Segundo Ejemplo Mejoranro
    def Loguin_Master(self, url, name, clave, t):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar(url, t)
        f.Text_Xpath_Validar("//input[contains(@id,'user-name')]", name, t)
        f.Text_Xpath_Validar("//input[contains(@id,'password')]", clave, t)
        f.Click_Xpath_Validar("//input[contains(@id,'login-button')]", t)
        f.Salida()

