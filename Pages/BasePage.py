from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def do_click(self, by_locator):
        try:
            self.wait.until(ec.visibility_of_element_located(by_locator)).click()
        except Exception as e:
            print(e)

    def do_sendKeys(self, by_locator, text):
        try:
            self.wait.until(ec.visibility_of_element_located(by_locator)).send_keys(text)
        except Exception as e:
            print(e)

    def get_page_title(self):
        try:
            return self.driver.title
        except Exception as e:
            print(e)

    def press_enter_key(self, by_locator):
        try:
            self.wait.until(ec.presence_of_element_located(by_locator)).send_keys(Keys.RETURN)
        except Exception as e:
            print(e)

    def scroll_to_element(self, by_locator):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", *by_locator)
        except Exception as e:
            print(e)

    def verifyElementIsPresent(self, by_locator):
        try:
            if(self.wait.until(ec.presence_of_element_located(by_locator))):
                return True
            else:
                return False
        except Exception as e:
            return False

    def get_element_count(self, by_locator):
        list = self.driver.find_elements(*by_locator)
        return len(list)

    def get_current_url(self):
        return self.driver.current_url









