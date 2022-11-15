import time
import unittest
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException

t = 2
#Creando funciones
class Funciones_Globales():

    #con esta funcion se inicializan las variables
    def __init__(self, driver):
        self.driver = driver

    #funcion que no regresa valor
    def saludos(self):
        print("Bienvenido a Page Object Model")

    def saludos2(self):
        print("Prueba saludo 2")

    #funcion que nos regrese un valor/resultado
    def Tiempo(self, tiempo):
        t = time.sleep(tiempo)
        return t

    def Navegar(self, url, tiempo):
        self.driver.get(url)
        self.driver.maximize_window()
        print("Pagina Abierta " + str(url))
        t = time.sleep(tiempo)
        return t

    def Text_Xpath(self, xpath, texto, tiempo, val):
        self.driver.find_element_by_xpath(xpath)
        val.clear()
        val.send_keys(texto)
        t = time.sleep(tiempo)
        return t

    def Text_Xpath_Validar(self, xpath, texto, tiempo):
        try:
            val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
            val = self.driver.find_element_by_xpath(xpath)
            val.clear()
            val.send_keys(texto)
            print("Escribiendo en el campo {} el texto {}".format(xpath, texto))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + xpath)
            return t

    def Click_Xpath_Validar(self, xpath, tiempo):
        try:
            val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
            val = self.driver.find_element_by_xpath(xpath)
            val.click()
            print("Damos click en el campo {} ".format(xpath))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + xpath)
            return t

    #Seccion 20.84 Funcion Select
    def Select_Xpath_Text(self, xpath, texto, tiempo):
        try:
            val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
            val = self.driver.find_element_by_xpath(xpath)
            val = Select(val)
            val.select_by_visible_text(texto)
            print("El campo seleccionado es {} ".format(texto))
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + xpath)
            return t

    # Funcion select XPATH ( agrega por index value text)
    def Select_Xpath_Type(self, xpath, tipo, dato, tiempo):
        try:
            # las tres lineas pasan a la funcion SEX
            # val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            # val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
            # val = self.driver.find_element_by_xpath(xpath)
            val = self.SEX(dato)
            val = Select(val)
            if (tipo == "text"):
                val.select_by_visible_text(dato)
            elif (tipo == "index"):
                val.select_by_index(dato)
            elif (tipo == "value"):
                val.select_by_value(dato)
            print("El campo seleccionado es {} ".format(dato))
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + xpath)
            return t



    def Text_Id(self, ID, texto, tiempo, val):
        self.driver.find_element_by_id(ID)
        val.clear()
        val.send_keys(texto)
        t = time.sleep(tiempo)
        return t

    def Text_Id_Validar(self, id, texto, tiempo):
        try:
            val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
            val = self.driver.find_element_by_xpath(id)
            val.clear()
            val.send_keys(texto)
            print("Escribiendo en el campo {} el texto {}".format(id, texto))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + id)
            return t

    def Click_Id_Validar(self, id, tiempo):
        try:
            val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
            val = self.driver.find_element_by_xpath(id)
            val.click()
            print("Damos click en el campo {} ".format(id))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + id)
            return t

    #Funcion select Id ( agrega por index value text)
    def Select_Id_Type(self, xpath, tipo, dato, tiempo):
        try:
            # las tres lineas pasan a la funcion SEX
            # val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, id)))
            # val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
            # val = self.driver.find_element_by_id(id)
            val = self.SEI(dato)
            val = Select(val)
            if(tipo=="text"):
                val.select_by_visible_text(dato)
            elif(tipo=="index"):
                val.select_by_index(dato)
            elif(tipo=="value"):
                val.select_by_value(dato)
            print("El campo seleccionado es {} ".format(dato))
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + xpath)
            return t

    #Funcion Upload Xpath
    def Upload_Xpath(self, xpath, ruta, tiempo):
        try:
            # las tres lineas pasan a la funcion SEX
            # val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            # val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
            # val = self.driver.find_element_by_xpath(xpath)
            val = self.SEX(ruta)
            val.send_keys(ruta)
            print("Se carga imagen {} ".format(ruta))
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + xpath)
            return t

    #Funcion Upload Id
    def Upload_Id(self, id, ruta, tiempo):
        try:
            # las tres lineas pasan a la funcion SEI
            # val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, id)))
            # val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
            # val = self.driver.find_element_by_id(id)
            val = self.SEI(ruta)
            val.send_keys(ruta)
            print("Se carga imagen {} ".format(ruta))
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + id)
            return t

    #Funcion Radio y Check Xpath
    def Check_Xpath(self, xpath, tiempo):
        try:
            # las tres lineas pasan a la funcion SEX
            # val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            # val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
            # val = self.driver.find_element_by_xpath(xpath)
            val = self.SEX(xpath)
            val.click()
            print("Click en el elemento {} ".format(xpath))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + xpath)
            return t

    #Funcion Radio y Check Id
    def Check_Id(self, id, tiempo):
        try:
            # las tres lineas pasan a la funcion SEI
            # val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, id)))
            # val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
            # val = self.driver.find_element_by_id(id)
            val = self.SEI(id)
            val.click()
            print("Click en el elemento {} ".format(id))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + id)
            return t

    #Multi Check Xpath
    def Multi_Check_Xpath(self, tiempo, *args):
        try:
            for multiple in args:
                # las tres lineas pasan a la funcion SEX
                # val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, multiple)))
                # val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
                # val = self.driver.find_element_by_xpath(multiple)
                val = self.SEX(multiple)
                val.click()
                print("Click en el elemento {} ".format(multiple))
                t = time.sleep(tiempo)
                return t
        except TimeoutException as ex:
            for multiple in args:
                print(ex.msg)
                print("No se encontro el elemento" + multiple)
                return t

    def Existe(self, tipo, selector, tiempo):
        if(tipo == "xpath"):
            try:
                # las tres lineas pasan a la funcion SEX
                # val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, selector)))
                # val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
                # val = self.driver.find_element_by_xpath(selector)
                val = self.SEI(selector)
                val.click()
                print("El elemento {} existe ".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
                return "No existe"
        elif(tipo == "id"):
            try:
                # las tres lineas pasan a la funcion SEI
                # val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, selector)))
                # val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
                # val = self.driver.find_element_by_id(selector)
                val = self.SEI(selector)
                val.click()
                print("El elemento {} existe ".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
                return "No existe"

    #Seleccionar Elemeto Xpath Seccion 24.110
    def SEX(self, elemento):
        val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
        val = self.driver.find_element_by_xpath(elemento)
        return val

    #Seleccionar Elemeto ID Seccion 24.110
    def SEI(self, elemento):
        val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
        val = self.driver.find_element_by_id(elemento)
        return val

    def Text_Mixto(self,tipo, selector, texto, tiempo):
        if(tipo == "xpath"):
            try:
                #las tres lineas pasan a la funcion SEX
                # val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, selector)))
                # val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
                # val = self.driver.find_element_by_xpath(selector)
                val = self.SEX(selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto {}".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                # las tres lineas pasan a la funcion SEI
                # val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, selector)))
                # val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
                # val = self.driver.find_element_by_id(selector)
                val = self.SEI(selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto {}".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
                return

    def Click_Mixto(self, tipo, selector, tiempo):
        if (tipo == "xpath"):
            try:
                # las tres lineas pasan a la funcion SEX
                # val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, selector)))
                # val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
                # val = self.driver.find_element_by_xpath(selector)
                val = self.SEX(selector)
                val.click()
                print("Damos click en el campo {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                # las tres lineas pasan a la funcion SEI
                # val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, selector)))
                # val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
                # val = self.driver.find_element_by_id(selector)
                val = self.SEI(selector)
                val.click()
                print("Damos click en el campo {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
                return t

    def Click_Doble(self,tipo, selector, tiempo):
        if(tipo == "xpath"):
            try:
                # las tres lineas pasan a la funcion SEX
                # val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, selector)))
                # val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
                # val = self.driver.find_element_by_xpath(selector)
                val = self.SEX(selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("Doble Click en {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                # las tres lineas pasan a la funcion SEI
                # val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, selector)))
                # val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
                # val = self.driver.find_element_by_id(selector)
                val = self.SEI(selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("Doble Click en {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
                return

    def Click_Derecho(self,tipo, selector, tiempo):
        if(tipo == "xpath"):
            try:
                # las tres lineas pasan a la funcion SEX
                # val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, selector)))
                # val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
                # val = self.driver.find_element_by_xpath(selector)
                val = self.SEX(selector)
                act = ActionChains(self.driver)
                act.context_click(val).perform()
                print("Click Derecho en {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                # las tres lineas pasan a la funcion SEI
                # val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, selector)))
                # val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
                # val = self.driver.find_element_by_id(selector)
                val = self.SEI(selector)
                act = ActionChains(self.driver)
                act.context_click(val).perform()
                print("Click Derecho en {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
                return

    def Drag_and_Drop(self,tipo, selector, destino, tiempo):
        if(tipo == "xpath"):
            try:
                # las tres lineas pasan a la funcion SEX
                # val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, selector)))
                # val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
                # val = self.driver.find_element_by_xpath(selector)
                val = self.SEX(selector)
                val2 = self.SEX(destino)
                act = ActionChains(self.driver)
                act.drag_and_drop(val, val2).perform()
                print("Se solto el elemento {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                # las tres lineas pasan a la funcion SEI
                # val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, selector)))
                # val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
                # val = self.driver.find_element_by_id(selector)
                val = self.SEI(selector)
                val2 = self.SEX(destino)
                act = ActionChains(self.driver)
                act.drag_and_drop(val, val2).perform()
                print("Se solto el elemento {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
                return

    def Drag_and_DropXY(self,tipo, selector, x,y, tiempo):
        if(tipo == "xpath"):
            try:
                # las tres lineas pasan a la funcion SEX
                # val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, selector)))
                # val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
                # val = self.driver.find_element_by_xpath(selector)
                self.driver.switch_to_frame(0)
                val = self.SEX(selector)
                act = ActionChains(self.driver)
                act.drag_and_drop_by_offset(val,x ,y).perform()
                print("Se solto el elemento {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                # las tres lineas pasan a la funcion SEI
                # val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, selector)))
                # val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
                # val = self.driver.find_element_by_id(selector)
                self.driver.switch_to_frame(0)
                val = self.SEI(selector)
                act = ActionChains(self.driver)
                act.drag_and_drop_by_offset(val,x ,y).perform()
                print("Se solto el elemento {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
                return

    def ClickXY(self, tipo, selector, x, y, tiempo=.2):
        if (tipo == "xpath"):
            try:
                # self.driver.switch_to.frame(0)
                val = self.SEX(selector)
                act = ActionChains(self.driver)
                act.move_to_element_with_offset(val, x, y).click().perform()
                print("Click al elemento{} coordenada {}, {}".format(selector, x, y))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                # self.driver.switch_to.frame(0)
                val = self.SEI(selector)
                act = ActionChains(self.driver)
                act.move_to_element_with_offset(val, x, y).click().perform()
                print("Click al elemento{} coordenada {}, {}".format(selector, x, y))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t


    def Salida(self):
        print("La prueba termina de forma exitosa")