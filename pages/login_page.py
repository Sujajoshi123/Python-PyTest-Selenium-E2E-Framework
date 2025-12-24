from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    #Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def login(self, username, password):
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)
        time.sleep(2)