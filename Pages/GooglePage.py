import time
from selenium.webdriver.common.by import By
from Config.TestData import TestData
from Pages.BasePage import BasePage
from Pages.ReqresPage import ReqresPage

class GooglePage(BasePage):

    #Locators
    search_field = (By.XPATH, "//input[@type='text']")
    link = (By.XPATH, "//h3[contains(text(), 'Reqres - A hosted REST-API')]")

    #Constructor
    def __init__(self, driver):
        super().__init__(driver)

    #Actions
    def sendkeys_and_enter(self):
        self.do_sendKeys(self.search_field, "reqres")
        self.press_enter_key(self.search_field)
        self.do_click(self.link)
        return ReqresPage(self.driver)




