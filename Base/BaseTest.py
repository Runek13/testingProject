import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select


class BaseTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()  # se declara diverul si ii setam calea
        # self.driver=webdriver.Chrome(executable_path="/home/theo/Downloads/chromedriver") #se declara diverul si ii setam calea
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://demo.automationtesting.in/Register.html")

    @classmethod
    def tearDown(self):
        self.driver.quit()
