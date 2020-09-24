import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from Base.BaseTest import BaseTest


class AlertsTest(BaseTest): #declararea clasei in care vom avea testele automate

    def test_Alert(self): #se face o metoda de test


    #Facem hower pe un element
        self.switchtomenu=self.driver.find_element_by_xpath("//a[contains(text(),'Switch')]")
        self.switchtoaction=ActionChains(self.driver)
        self.switchtoaction.move_to_element(self.switchtomenu).perform()
        self.alerts=self.driver.find_element_by_xpath("//a[contains(text(),'Alerts')]")
        self.alerts.click()

        #declaram o lista
        self.alertslist=self.driver.find_elements_by_xpath("//ul[@class='nav nav-tabs nav-stacked']/li/a")
        self.alertslist[0].click()
        self.buttons=self.driver.find_elements_by_xpath("//button[contains(text(),'click the button')]")
        self.buttons[0].click()

        #interactionam cu alerte
        self.alert1=WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.alerttext=self.alert1.text
        print(self.alerttext)
        self.alert1.accept()
        self.alertslist[1].click()
        self.buttons[1].click()
        self.alert2=WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        print(self.alert2.text)
        self.alert2.dismiss()
        self.alertslist[2].click()
        self.buttons[2].click()
        self.alert3=WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        print(self.alert3.text)
        self.alert3.send_keys("Ceva scris aici")
        self.alert3.accept()
        time.sleep(5)




