from NavigoPlatform.CommonBase.BasePage import BasePage
from selenium.webdriver.common.by import By
from NavigoPlatform.Configurations.Config import TestConfig


class LoginPage(BasePage):
    LocTxtUsername = (By.ID, "username")
    LocTxtPassword = (By.ID, "password")
    LocBtnLogin = (By.ID, "kc-login")
    LocMsgInvalidCreds = (By.CLASS_NAME, "kc-feedback-text")
    user = TestConfig.USERNAME
    pwd = TestConfig.PASSWORD

    def __init__(self,driver):
        super().__init__(driver)

    def enter_login_credentials(self):
        self.input_element(self.LocTxtUsername, LoginPage.user)
        self.input_element(self.LocTxtPassword, LoginPage.pwd)

    def enter_username(self, user):
        self.input_element(self.LocTxtUsername, user)

    def enter_password(self, pwd):
        self.input_element(self.LocTxtPassword, pwd)

    def enter_login(self):
        self.click_on_element(self.LocBtnLogin)

    def validate_title(self):
        assert self.get_title() == "Navigo Platform"

    def validate_invalid_creds(self):
        if self.get_element_by_text(self.LocMsgInvalidCreds) == "Invalid username or password.":
            self.take_screenshot()
            assert True
        else:
            assert False, "Something went wrong with invalid creds. Please check"

    def validate_empty_username(self):
        assert self.get_element_by_text(self.LocMsgInvalidCreds) == "Invalid username or password."

    #
    # def validateEmptyPassword(self):
    #     assert self.get_element_text(self.MSG_INVALIDCREDS) == "Password cannot be empty"
