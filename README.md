# PythonSelenium

Overview:

Selenium Hybrid Framework
(python, Selenium, pytest, Page Object Model, HTML reports)

Techstack Used:-

Selenium - Selenium Libraries
Pytest - Python Unit Test Framework
pytest-html - PyTest HTML reports
pytest-xdist - Run test parallel


The project contains below folder structure
Config(package) -- TestData - It contains the common data which can be utilized through out the project. e,g URL,searchdata etc.

Pages(package)

1.BasePage(class)
This class contains the basic selenium actions which will be needed during the test case execution.
For e.g click on webelement, scroll to particular element, send data to input field, explicit wait etc

2.GooglePage(classs)
This contains the google page webelements and actions that needs to perform with the help of it.
e.g search operation, click on searched result.

3.ReqresPage(class)
This contains the reqres page webelements and actions that needs to perform with the help of it.
e.g verify page title, get request count etc

Test(package)

1.conftest(class)
It is the most imp class as it contains web driver initialization configuration.Test case execution start from this class as its been extend by BaseTest class.

2.TestBase(class)
This class will be using init_driver function of conftest file using fixture functionality.This class will be extended by the test case to start the exectuin part.

3.Test_Reqres(class)
It it a test class which contain a test case (test_google_enter_search_key) which will perform the expected functionality.


How to run the test case:
Go to Tests(package).
Right click on Test_Reqres class -> Run as Python Test for Test_Reqres.
Validate the functionality.


