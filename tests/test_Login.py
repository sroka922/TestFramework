import datetime
import time

import pytest
from selenium.webdriver.common.by import By
from datetime import datetime

from Pages.AccountPage import AccountPage
from Pages.HomePage import HomePage, credentials_data
from Pages.LoginPage import LoginPage


def generate_email_with_timestamp():
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "amotoori" + time_stamp + "@gmail.com"


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def test_login_with_valid_credentials(self):
        HomePage(self.driver) \
            .click_on_MyAccount() \
            .click_on_Login()
        LoginPage(self.driver) \
            .input_login("amotooricap@gmail.com") \
            .input_password() \
            .click_login()
        assert AccountPage.myAccount.__eq__("Edit your account information")

    def test_login_with_invalid_credentials(self):
        HomePage(self.driver) \
            .click_on_MyAccount() \
            .click_on_Login()
        login_page = LoginPage(self.driver) \
            .input_login(generate_email_with_timestamp()) \
            .input_password() \
            .click_login()
        assert login_page.lack_of_credentials() == "Warning: No match for E-Mail Address and/or Password."

    @pytest.mark.parametrize("email,password", credentials_data)
    def test_login_with_invalid_password(self, email,password):
        HomePage(self.driver) \
            .click_on_MyAccount() \
            .click_on_Login()
        login_page = LoginPage(self.driver) \
            .input_login(email) \
            .input_password(password) \
            .click_login()
        assert login_page.lack_of_credentials() == "Warning: No match for E-Mail Address and/or Password."

    def test_login_without_any_credentials(self):
        loginPage = HomePage(self.driver) \
            .click_on_MyAccount() \
            .click_on_Login()
        loginPage.input_login("") \
            .input_Empty_password() \
            .click_login()
        assert (loginPage.lack_of_credentials() == "Warning: No match for E-Mail Address and/or Password.")
