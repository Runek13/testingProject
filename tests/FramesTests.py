import time
from Help.ElementMethods import ElementMethods
from Base.BaseTest import BaseTest


class FramesTest(BaseTest):  # declararea clasei in care vom avea testele automate

    def test_frames(self):  # se face o metoda de test
        self.element_methods = ElementMethods(self.driver)

        self.switch_to_menu = self.driver.find_element_by_xpath("//a[contains(text(),'Switch')]")
        self.element_methods.HowerElement(self.switch_to_menu)
        self.frames = self.driver.find_element_by_xpath("//a[contains(text(),'Frames')]")
        self.frames.click()

        self.element_methods.clickListElement("//ul[@class='nav nav-tabs ']/li/a")

        # ma mut cu actiunea pe iframe

        self.driver.switch_to.frame("singleframe")
        self.element_methods.sendKeysForElement("alabala")
        self.driver.switch_to.default_content()

        self.element_methods.clickListElement("//ul[@class='nav nav-tabs ']/li/a", 1)

        self.element_methods.iframeWaitWebDriver("MultipleFrames")
        self.element_methods.iframeWaitWebDriver("SingleFrame")

        self.element_methods.sendKeysForElement("askdjas")
