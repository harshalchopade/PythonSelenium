from Pages.GooglePage import GooglePage
import TestBase

class Test_Reqres(TestBase):
    def test_google_enter_search_key(self):
        self.googlePage = GooglePage(self.driver)
        reqres_object = self.googlePage.sendkeys_and_enter()
        reqres_object.verifyFunctionalityOfRegresPage()


