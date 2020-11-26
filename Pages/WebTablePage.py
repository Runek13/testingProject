from Pages.BasePage import BasePage


class WebTablePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.pageMethods.ValidateTitlePage("Web Table")