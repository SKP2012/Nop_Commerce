# from selenium import webdriver  -- No needed here
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[normalize-space()='Log in']"
    link_logout_linktext = "Logout"

    # This class encapsulates the login page actions for a web application.
    # It provides methods to set the username and password, click the login button, and click the logout link.
    # Constructor initializes the driver, hence create constructor to pass the driver instance.
    # Also create another constructors
    # to set the username and password directly if needed.

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys("password")

    def clickLogin(self):

        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clickLogout(self):

        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()