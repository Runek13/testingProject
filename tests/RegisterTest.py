import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#se declara framework-urile care se includ in test

class RegisterTest(unittest.TestCase): #declararea clasei in care vom avea testele automate

    def test_Register(self): #se face o metoda de test
        self.driver=webdriver.Chrome(executable_path="/home/theo/Downloads/chromedriver") #se declara diverul si ii setam calea
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://demo.automationtesting.in/Register.html") #accesam un anumit url

        #validam pagina pe care ne aflam

        self.expectedregisterpage="Register"
        self.actualregisterpage=self.driver.title  #metoda care returneaza titlul paginii pe care se afla driverul
        self.errormessage="titlul paginii not ok"
        assert self.expectedregisterpage==self.actualregisterpage,self.errormessage

        #completam fieldul de first name si last name (radiobox)
        self.firstnameweb=self.driver.find_element_by_xpath("//input[@placeholder='First Name']")
        self.firstnameweb.send_keys("abc")
        self.lastnameweb=self.driver.find_element_by_xpath("//input[@placeholder='Last Name']")
        self.lastnameweb.send_keys("cba")
        self.addressweb=self.driver.find_element_by_xpath("//textarea")
        self.addressweb.send_keys("usdjfggs")
        self.emailaddressweb = self.driver.find_element_by_xpath("//input[@ng-model='EmailAdress']")
        self.emailaddressweb.send_keys("jhfdhds@gmail.com")
        self.phonenumberweb=self.driver.find_element_by_xpath("//input[@type='tel']")
        self.phonenumberweb.send_keys("8473754634")



        #selectam un gen (checkbox)
        self.genmaleweb=self.driver.find_element_by_xpath("//input[@value='Male']")
        self.genmaleweb.click()

        #selectam un hobby
        self.cricket=self.driver.find_element_by_xpath("//input[@value='Cricket']")
        self.cricket.click()

        #alegem valoarea dintr-un dropdown
        self.countryweb=self.driver.find_element_by_id("countries")
        self.countrydropdown=Select(self.countryweb)
        self.countrydropdown.select_by_visible_text("Romania")
        self.yearweb=self.driver.find_element_by_id("yearbox")
        self.yeardropdown=Select(self.yearweb)
        self.yeardropdown.select_by_value("1994")
        self.monthweb=self.driver.find_element_by_xpath("//select[@placeholder='Month']")
        self.monthdropdown=Select(self.monthweb)
        self.monthdropdown.select_by_visible_text("August")
        self.dayweb=self.driver.find_element_by_xpath("//select[@placeholder='Day']")
        self.daydropdown=Select(self.dayweb)
        self.daydropdown.select_by_value("2")
        self.passwordweb=self.driver.find_element_by_id("firstpassword")
        self.passwordweb.send_keys("Qwerty1")
        self.confirmpasswordweb=self.driver.find_element_by_id("secondpassword")
        self.confirmpasswordweb.send_keys("Qwerty1")
        self.submitweb=self.driver.find_element_by_id("submitbtn")
        self.submitweb.click()

        self.driver.find_element_by_xpath("//body[@ng-controller='gridctrl']")
        self.expectednextpage="Web Table"
        self.actualnextpage=self.driver.title  # metoda care returneaza titlul paginii pe care se afla driverul
        self.errormessage="titlul paginii nu e bun"
        assert self.expectednextpage == self.actualnextpage, self.errormessage





        time.sleep(5)




