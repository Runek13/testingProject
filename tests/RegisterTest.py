import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time

from Base.BaseTest import BaseTest
# se declara framework-urile care se includ in test
from ExcelUtility.ExcelUtility import ExcelUtility
from Help.ElementMethods import ElementMethods
from Help.PageMethods import PageMethods
from Pages.RegisterPage import RegisterPage


class RegisterTest(BaseTest):  # declararea clasei in care vom avea testele automate
    driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_Register(self):  # se face o metoda de test
        # declaram un obiect de tipul elementmethod pentru a folosi metodele generale
        self.elementmethods = ElementMethods(self.driver)
        self.pagemethods = PageMethods(self.driver)

        #declaram un obiect de tipul excel de la o anumita locatie si cu un sheet specific
        self.excelUtility = ExcelUtility("../Libre/DataDrivenTesting.xlsx", "ForRegister")

        # validam pagina pe care ne aflam


        # completam fieldul de first name si last name (radiobox)
        self.registerPage = RegisterPage(self.driver)
        self.registerPage.registerProcess(self.excelUtility.readDataByIndex(2, 2), "Buna")
        #dupa ce am terminat de declarat elementele+elementul submit
        #self.registerPage.clickSubmit()



        self.addressweb = self.driver.find_element_by_xpath("//textarea")
        self.elementmethods.WriteElement(self.addressweb, "sjhasgd")

        self.emailaddressweb = self.driver.find_element_by_xpath("//input[@ng-model='EmailAdress']")
        self.elementmethods.WriteElement(self.emailaddressweb, self.excelUtility.readDataByIndex(4, 2))

        self.phonenumberweb = self.driver.find_element_by_xpath("//input[@type='tel']")
        self.elementmethods.WriteElement(self.phonenumberweb, "3475322958")

        # selectam un gen (checkbox)

        # selectam un hobby
        self.cricket = self.driver.find_element_by_xpath("//input[@value='Cricket']")
        self.elementmethods.ClickElement(self.cricket)

        # alegem valoarea dintr-un dropdown
        self.countryweb = self.driver.find_element_by_id("countries")
        self.elementmethods.SelectElementByText(self.countryweb, "Romania")

        self.yearweb = self.driver.find_element_by_id("yearbox")
        self.elementmethods.SelectElementByValue(self.yearweb, "1994")

        self.monthweb = self.driver.find_element_by_xpath("//select[@placeholder='Month']")
        self.elementmethods.SelectElementByText(self.monthweb, "August")

        self.dayweb = self.driver.find_element_by_xpath("//select[@placeholder='Day']")
        self.elementmethods.SelectElementByValue(self.dayweb, "2")

        self.passwordweb = self.driver.find_element_by_id("firstpassword")
        self.elementmethods.WriteElement(self.passwordweb, "Qwerty1")

        self.confirmpasswordweb = self.driver.find_element_by_id("secondpassword")
        self.elementmethods.WriteElement(self.confirmpasswordweb, "Qwerty1")

        self.submitweb = self.driver.find_element_by_id("submitbtn")
        self.elementmethods.ClickElement(self.submitweb)

        self.driver.find_element_by_xpath("//body[@ng-controller='gridctrl']")
        self.expectednextpage = "Web Table"
        self.pagemethods.ValidateTitlePage(self.expectednextpage)

        time.sleep(5)
