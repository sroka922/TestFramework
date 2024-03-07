import time
from datetime import datetime

import pytest
from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from Pages.RegisterPage import RegisterPage


def generate_email_with_timestamp():
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "amotoori" + time_stamp + "@gmail.com"


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:
    def test_register_with_mandatory_fields(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Register']").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.ID, "input-firstname").send_keys("test")
        self.driver.find_element(By.ID, "input-lastname").send_keys("12345")
        self.driver.find_element(By.ID, "input-email").send_keys(generate_email_with_timestamp())
        self.driver.find_element(By.ID, "input-telephone").send_keys("123456789")
        self.driver.find_element(By.ID, "input-password").send_keys("12345")
        self.driver.find_element(By.ID, "input-confirm").send_keys("12345")
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "#content > h1").is_displayed()
        assert self.driver.find_element(By.CSS_SELECTOR, "#content > h1").text.__eq__("Your Account Has Been Created!")

    def test_register_with_all_fields(self):
        homePage = HomePage(self.driver)
        homePage.click_on_MyAccount()
        self.driver.find_element(By.XPATH, "//a[text()='Register']").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.ID, "input-firstname").send_keys("test")
        self.driver.find_element(By.ID, "input-lastname").send_keys("12345")
        self.driver.find_element(By.ID, "input-email").send_keys(generate_email_with_timestamp())
        self.driver.find_element(By.ID, "input-telephone").send_keys("123456789")
        self.driver.find_element(By.ID, "input-password").send_keys("12345")
        self.driver.find_element(By.ID, "input-confirm").send_keys("12345")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='newsletter'][value='1']").click()
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "#content > h1").is_displayed()
        assert self.driver.find_element(By.CSS_SELECTOR, "#content > h1").text.__eq__("Your Account Has Been Created!")

    def test_register_with_existing_email(self):
        homePage = HomePage(self.driver)
        homePage.click_on_MyAccount()
        homePage.click_on_register()
        registerPage = RegisterPage(self.driver) \
            .input_firstname("name")\
            .input_lastname("lastname")\
            .input_email("amotooricap@gmail.com")\
            .input_telephone("123456789")\
            .input_password("passsword")\
            .input_confirm_password("passsword")\
            .agree_privacy_policy() \
            .subscribe_newsletter() \
            .click_continue()
        assert registerPage.display_alert().is_displayed()
        assert (registerPage.display_alert().text
                .__eq__("Warning: E-Mail Address is already registered!"))

    def test_register_without_providing_any_data(self):
        homePage = HomePage(self.driver)
        homePage.click_on_MyAccount()
        homePage.click_on_register()
        registerPage = RegisterPage(self.driver) \
            .input_firstname("")\
            .input_lastname("")\
            .input_email("")\
            .input_telephone("")\
            .input_password("")\
            .input_confirm_password("")\
            .agree_privacy_policy() \
            .subscribe_newsletter() \
            .click_continue()
        assert (registerPage.get_first_name_alert()
                .__eq__("First Name must be between 1 and 32 characters!"))
        assert (registerPage.get_last_name_alert()
                .__eq__("Last Name must be between 1 and 32 characters!"))
        assert (registerPage.get_email_alert()
                .__eq__("E-Mail Address does not appear to be valid!"))
        assert (registerPage.get_password_alert()
                .__eq__("Password must be between 4 and 20 characters!"))

    def test_register_with_bad_password_confirmation(self):
        homePage = HomePage(self.driver)
        homePage.click_on_MyAccount()
        homePage.click_on_register()
        registerPage = RegisterPage(self.driver) \
            .input_firstname("name")\
            .input_lastname("lastname")\
            .input_email("email@o2.pl")\
            .input_telephone("123456789")\
            .input_password("123456")\
            .input_confirm_password("12345b")\
            .agree_privacy_policy() \
            .subscribe_newsletter() \
            .click_continue()
        assert (self.driver.find_element(By.CSS_SELECTOR, "#input-confirm + .text-danger")
                .text.__eq__("Password confirmation does not match password!"))
