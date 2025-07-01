import time
import pytest
from selenium import webdriver

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen  # Importing the custom logger if we need to record logs
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".\\testData\\LoginData.xlsx"
    logger = LogGen.loggen()  # Initialize the logger as logger returns value from the loggen method in customLogger.py

    def test_login(self, setup):
        self.logger.info("******** Test_002_DDT_Login ********")
        self.logger.info("******** Verifying login test********")
        self.driver = setup  # Initialize the Chrome driver
        self.driver.get(self.baseURL)  # Navigate to the base URL
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in the Excel file: ", self.rows)
        # Loop through each row in the Excel file to read/capture the data and send it to login page:
        for r in range(2, self.rows + 1):
            self.username = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)  # Expected result from the Excel file

            # Now passing/sending the values:
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            # Clicking on login  button:
            self.lp.clickLogin()
            time.sleep(5)

            # Verifying the title after login to check if login is successful or not:
            # Getting the actual title after login:
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            lst_status = []  # List to store the status of each login attempt
            if act_title == exp_title:
                if self.exp == "Pass":
                    assert True
                    self.logger.info("******** Login test passed ********")
                    self.lp.clickLogout()
                    lst_status.append("Pass")  # Append "Pass" to the list if login is successful
                elif self.exp == "Fail":
                    assert False
                    self.logger.error("******** Login test failed ********")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            # If the actual title does not match the expected title:
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.error("******** Login test failed ********")
                    assert False
                elif self.exp == "Fail":
                    self.logger.info("******** Login test passed ********")
                    assert True

        if Fail not in lst_status:
            self.logger.info("******** Login test completed successfully ********")
            self.driver.close()
            assert True  # If all login attempts were successful, assert True
        else:
            self.logger.error("******** Login test failed ********")
            self.driver.close()
            assert False # If any login attempt failed, assert False

        self.logger.info("******** Completed all login tests ********")