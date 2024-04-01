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
t=2




def test_login_uno():
    driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    fl = Funciones_Login(driver)
    fl.L1("juan@gmail.com","12345776","No customer account found",t)
    fl.L2("rodrigo","23456","Wrong email")
    fl.l3("admin@yourstore.com","admin","Dashboard")



















