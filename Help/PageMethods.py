import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class PageMethods:
    def __init__(self, driver):
        self.driver = driver

    # validam pagina pe care ne aflam
    def ValidateTitlePage(self, expected):
        WebDriverWait(self.driver, 10).until(EC.title_is(expected))
        actualregisterpage = self.driver.title  # metoda care returneaza titlul paginii pe care se afla driverul
        errormessage = "titlul paginii not ok"
        assert expected == actualregisterpage, errormessage

    def switchBetweenWindows(self):
        number_of_tabs = self.driver.window_handles
        print(number_of_tabs)
        self.driver.switch_to.window(number_of_tabs[1])
        print(self.driver.title)
        self.driver.find_element_by_id("dropdownButton")
        self.ValidateTitlePage("SeleniumHQ Browser Automation")
        self.driver.close()
        self.driver.switch_to.window(number_of_tabs[0])

    def processWindows(self, index):
        windowlist = self.driver.find_elements_by_xpath("//ul[@class='nav nav-tabs nav-stacked']/li/a")
        windowlist[index].click()
        buttons = self.driver.find_elements_by_xpath("//button[contains(text(),'click')]")
        buttons[index].click()