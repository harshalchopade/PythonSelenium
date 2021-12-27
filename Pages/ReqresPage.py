import json
import requests
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class ReqresPage(BasePage):
    #Locator
    endpoint = None
    subtitle = (By.XPATH, "//h2[.='Give it a try']")
    request_list = (By.XPATH, "//li[contains(@data-http,'get')]")
    list_users = (By.XPATH, "//li[@data-id='users']")
    request_api_box = (By.XPATH, "//span[.='/api/users?page=2']")

    #Constructor
    def __init__(self, driver):
        super().__init__(driver)

    #Actions
    def verifyPageTitle(self):
        actual_title = self.get_page_title()
        assert actual_title == "Reqres - A hosted REST-API ready to respond to your AJAX requests"

    # def verifySubtitlePresent(self):
    #     self.scroll_to_element(self.subtitle)

    def verifySubtitleIsPresent(self):
        assert self.verifyElementIsPresent(self.subtitle)

    def getElementCount(self):
        count = self.get_element_count(self.request_list)
        print("\n Element count is: ", count)
        assert count == 7

    def clickOnListUsersAndRequestBox(self):
        self.do_click(self.list_users)
        self.do_click(self.request_api_box)

    def get_end_point(self):
        ReqresPage.endpoint = self.get_current_url()
        print("\n EndPoint URL is: ",ReqresPage.endpoint)

    def verify_endpoint(self):
        r = requests.get(ReqresPage.endpoint)
        data = json.loads(r.content)
        #print(data)
        assert data['total'] == 12 and r.status_code == 200

    def verifyFunctionalityOfRegresPage(self):
        self.verifyPageTitle()
        self.verifySubtitleIsPresent()
        self.getElementCount()
        self.clickOnListUsersAndRequestBox()
        self.get_end_point()
        self.verify_endpoint()


