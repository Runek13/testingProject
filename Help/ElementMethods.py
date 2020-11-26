import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ElementMethods:
    # facem constructor
    def __init__(self, driver):
        self.driver = driver

    # metoda generala pentru click
    def ClickElement(self, element):
        element.click()

    # metoda pentru scris
    def WriteElement(self, element, value):
        element.send_keys(value)

    def SelectElementByText(self, element, value):
        self.elementdropdown = Select(element)
        self.elementdropdown.select_by_visible_text(value)

    def SelectElementByValue(self, element, value):
        self.elementdropdown = Select(element)
        self.elementdropdown.select_by_value(value)

    def HowerElement(self, element):
        self.action = ActionChains(self.driver)
        self.action.move_to_element(element).perform()

    def clickListElement(self, list_path, element_number=0):
        list = self.driver.find_elements_by_xpath(list_path)
        list[element_number].click()

    def interactionWithAlerts(self, accept=True):
        alert_element = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert_text = alert_element.text
        print(alert_text)
        if accept is True:
            alert_element.accept()
        else:
            alert_element.dismiss()

    def iframeWaitWebDriver(self, iframe_name, seconds=10):
        web_driver_wait = WebDriverWait(self.driver, seconds)
        xpath = "//iframe[@src='{}.html']".format(iframe_name)
        element = self.driver.find_element_by_xpath(xpath)
        available_and_switch = EC.frame_to_be_available_and_switch_to_it(element)
        web_driver_wait.until(available_and_switch)

    def sendKeysForElement(self, words, xpath="//input[@type='text']"):
        inputfield = self.driver.find_element_by_xpath(xpath)
        inputfield.send_keys(words)
        time.sleep(5)

