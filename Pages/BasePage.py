from Help.ElementMethods import ElementMethods
from Help.PageMethods import PageMethods


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

        self.elementMethods = ElementMethods(self.driver)
        self.pageMethods = PageMethods(self.driver)