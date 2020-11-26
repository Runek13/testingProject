import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from Base.BaseTest import BaseTest
from Help.ElementMethods import ElementMethods
from Help.PageMethods import PageMethods


class AlertsTest(BaseTest):  # declararea clasei in care vom avea testele automate

    def test_Alert(self):  # se face o metoda de test
        self.element_methods = ElementMethods(self.driver)
        self.page_methods = PageMethods(self.driver)
        self.page_methods.ValidateTitlePage("Register")

        # Facem hower pe un element
        self.switch_to_menu = self.driver.find_element_by_xpath("//a[contains(text(),'Switch')]")
        self.element_methods.HowerElement(self.switch_to_menu)

        self.alerts = self.driver.find_element_by_xpath("//a[contains(text(),'Alerts')]")
        self.element_methods.ClickElement(self.alerts)

        #  selectam primul element din lista
        self.element_methods.clickListElement("//ul[@class='nav nav-tabs nav-stacked']/li/a")
        self.element_methods.clickListElement("//button[contains(text(),'click the button')]")

        # interactionam cu alerte
        self.element_methods.interactionWithAlerts()
        alerts_list_path = "//ul[@class='nav nav-tabs nav-stacked']/li/a"
        buttons_list_path= "//button[contains(text(),'click the button')]"
        self.element_methods.clickListElement(alerts_list_path, 1)
        self.element_methods.clickListElement(buttons_list_path, 1)
        # self.alertslist[1].click()
        # self.buttons[1].click()

        self.element_methods.interactionWithAlerts(False)
        # trebuie sa declar mesajul care apare pe pagina
        # iau textul de pe mesaj/element
        self.element_methods.clickListElement(alerts_list_path, 2)
        self.element_methods.clickListElement(buttons_list_path, 2)
        # self.alertslist[2].click()
        # self.buttons[2].click()
        #
        # self.alert3 = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        # print(self.alert3.text)
        # self.alert3.send_keys("Ceva scris aici")
        # self.alert3.accept()
        time.sleep(5)
