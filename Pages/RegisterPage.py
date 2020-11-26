from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Pages.WebTablePage import WebTablePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.pageMethods.ValidateTitlePage("Register")

    #declaram webelementele
    __firstNameIdentifier = (By.XPATH, "//input[@placeholder='First Name']")
    __lastNameIdentifier = (By.XPATH, "//input[@placeholder='Last Name']")
    __genderIdentifier = (By.XPATH, "//input[@value='Male']")



    def __getFirstNameEelement(self):
        return self.driver.find_element(*RegisterPage.__firstNameIdentifier)
    def __getLastNameElement(self):
        return self.driver.find_element(*RegisterPage.__lastNameIdentifier)
    def __getGenderElement(self):
        return self.driver.find_element(*RegisterPage.__genderIdentifier)



    #declaram metode pt elementele din aceasta pagina
    def registerProcess(self, first_name_value, last_name_value):
        self.elementMethods.WriteElement(self.__getFirstNameEelement(), first_name_value)
        self.elementMethods.WriteElement(self.__getLastNameElement(), last_name_value)
        self.elementMethods.ClickElement(self.__getGenderElement())



    def clickSubmit(self):
        #declar elementul de submit, dau click pe el
        return WebTablePage(self.driver)