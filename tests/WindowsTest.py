import time
from Base.BaseTest import BaseTest
from Help.ElementMethods import ElementMethods
from Help.PageMethods import PageMethods


class WindowsTest(BaseTest):  # declararea clasei in care vom avea testele automate

    def test_WindowsTest(self):
        self.elementmethods = ElementMethods(self.driver)
        self.pagemethods = PageMethods(self.driver)
        self.switchtomenu = self.driver.find_element_by_xpath("//a[contains(text(),'Switch')]")
        self.elementmethods.HowerElement(self.switchtomenu)
        self.alerts = self.driver.find_element_by_xpath("//a[contains(text(),'Windows')]")
        self.alerts.click()
        self.pagemethods.processWindows(0)
        print(self.driver.title)
        self.pagemethods.ValidateTitlePage("Frames & windows")

        # ma mut cu actiunea pe noul tab
        self.pagemethods.switchBetweenWindows()
        self.pagemethods.processWindows(1)
        self.pagemethods.switchBetweenWindows()
        self.pagemethods.processWindows(2)
        time.sleep(5)


