import datetime
import time

import pytest
from selenium.webdriver.common.by import By
from datetime import datetime


def generate_email_with_timestamp():
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "amotoori" + time_stamp + "@gmail.com"


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def test_login_with_valid_credentials(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Login']").click()
        self.driver.find_element(By.ID, "input-email").send_keys("amotooricap@gmail.com")
        self.driver.find_element(By.ID, "input-password").send_keys("12345")
        self.driver.find_element(By.CSS_SELECTOR, "input[type=submit].btn").click()
        assert (self.driver.find_element(By.CSS_SELECTOR, "#content a[href*='account/edit']")
                .text.__eq__("Edit your account information"))

    def test_login_with_invalid_credentials(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.ID, "input-email").send_keys(generate_email_with_timestamp())
        self.driver.find_element(By.ID, "input-password").send_keys("12345")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        self.driver.implicitly_wait(2)
        assert self.driver.find_element(By.CSS_SELECTOR, "div.alert").is_displayed()
        time.sleep(2)

    def test_login_without_any_credentials(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Login']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[type=submit].btn").click()
        assert (self.driver.find_element(By.CSS_SELECTOR, ".alert-dismissible")
                .text.__eq__("Warning: No match for E-Mail Address and/or Password."))
