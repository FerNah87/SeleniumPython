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

def setup_function(function):
    print("Esto va al inicio de cada test \n")

def teardown_function(function):
    print("Esto es  al final de cada Test \n")


def test_uno():
    print("Test uno")



def test_dos():
    print("Test dos")




def test_tres():
    print("Test tres")



def test_cuatro():
    print("Test cuatro")