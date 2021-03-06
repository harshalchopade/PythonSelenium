import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Config.TestData import TestData

@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
        if request.param == "chrome":
            web_driver = webdriver.Chrome(ChromeDriverManager().install())
            web_driver.maximize_window()
            web_driver.get(TestData.URL)
        if request.param == "firefox":
            web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            web_driver.maximize_window()
            web_driver.get(TestData.URL)
        request.cls.driver = web_driver

        yield
        web_driver.close()
