import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen  # Importing the custom logger if we need to record logs

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword() # Replacing all static values with dynamic values/methods from the config file.

    logger = LogGen.loggen()  # Initialize the logger as logger returns value from the loggen method in customLogger.py

    @pytest.mark.sanity
    def test_homePageTitle(self,setup):
        self.logger.info("******** Test_001_Login ********") # we must user 1st log message of testcase Id
        self.logger.info("******** Verifying home page tile ********") # any test idea
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "your store. Login":
            assert True
            self.driver.close()
            self.logger.info("******** Home page title is verified ********") # Log message to indicate that the home page title is verified
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")  # \\ represents location in Windows
            assert False
            self.driver.close()
            self.logger.error("******** Home page title is not verified ********") # Log message to indicate that the home page title is not verified

    @pytest.mark.regression
    def test_login(self,setup):
        self.driver = setup  # Initialize the Chrome driver
        self.driver.get(self.baseURL) # Navigate to the base URL
        self.lp = LoginPage(self.driver) # Create an object instance i.e. 'lp' of LoginPage to call methods
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_login.png")  # \\ represents location in Windows
            self.driver.close()
            assert False
