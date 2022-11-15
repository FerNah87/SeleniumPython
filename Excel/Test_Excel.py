import time
import unittest
from Funciones_Excel import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
from Funciones.Funciones import Funciones_Globales

tg = 1

class base_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\SeleniumDrivers\chromedriver.exe")
        # self.driver = webdriver.Firefox(executable_path="C:\SeleniumDrivers\geckodriver.exe")

    def test1(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        fe = FunExcel(driver)
        f.Navegar("https://demoqa.com/text-box", tg)
        ruta = "C://Users//Fer - Patagonia//Python//SeleniumPython//Excel//Datos_ok.xlsx"
        filas = fe.getRowCount(ruta, "Hoja1")

        for r in range(2, filas+1):
            nombre = fe.readData(ruta, "Hoja1", r, 1)
            email = fe.readData(ruta, "Hoja1", r, 2)
            dir1 = fe.readData(ruta, "Hoja1", r, 3)
            dir2 = fe.readData(ruta, "Hoja1", r, 4)

            f.Texto_Mixto("id", "userName", nombre, tg)
            f.Texto_Mixto("id", "userEmail", nombre, tg)
            f.Texto_Mixto("id", "currentAddress", nombre, tg)
            f.Texto_Mixto("id", "submit", nombre, tg)

            e = f.Existe("id", "name", tg)
            if(e == "Existe"):
                print("El elemento se inserto correctamente")
                fe.writeData(ruta, "Hoja1", r, 5, "Insertado")
            else:
                print("No se inserto")
                fe.writeData(ruta, "Hoja1", r, 5, "Error")