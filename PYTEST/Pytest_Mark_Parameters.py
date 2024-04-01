import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones import Funciones_Globales
from Page_Login import Funciones_Login
from selenium.webdriver import ActionChains
t=.8


def get_Data():
    return [
        ("rodrigo","1234"),
        ("juan", "1233234"),
        ("pedro", "12232334"),
        ("erika", "1234232"),
        ("carlos", "1234sdf"),
        ("Admin", "admin123")
    ]


@pytest.mark.login
@pytest.mark.parametrize("user,clave",get_Data())
def test_login(user,clave):
    global driver
    driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f = Funciones_Globales(driver)
    f.Texto_Mixto("id", "txtUsername", user, t)
    f.Texto_Mixto("id", "txtPassword", clave, t)
    f.Click_Mixto("id", "btnLogin", t)
    print("Entrando al sistema")


def teardown_function():
    print("Salida del test")
    driver.close()

