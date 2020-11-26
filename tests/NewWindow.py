import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class NewWindow(unittest.TestCase):
    def test_NewWindow(self):
        self.driver=webdriver.Chrome(executable_path="/home/theo/Downloads/chromedriver") #se declara diverul si ii setam calea
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://www.google.com/")

        self.expectedregisterpage = "Google"
        self.actualregisterpage = self.driver.title  # metoda care returneaza titlul paginii pe care se afla driverul
        self.errormessage = "titlul paginii nu e ok"
        assert self.expectedregisterpage == self.actualregisterpage, self.errormessage

        time.sleep(5)