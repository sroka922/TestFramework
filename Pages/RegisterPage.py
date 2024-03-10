import json

from selenium.webdriver.common.by import By
from functools import wraps

from helpers.TestDataFactory import TestDataFactory



class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    firstname = "input-firstname"
    lastname = "input-lastname"
    email = "input-email"
    telephone = "input-telephone"
    password = "input-password"
    confirm_password = "input-confirm"
    newsletter = "input[name='newsletter'][value='1']"
    agree_policy = "agree"
    next = ".btn-primary"
    alert = ".alert-dismissible"

    firstname_alert = "#input-firstname  + .text-danger"
    lastname_alert = "#input-lastname+ .text-danger"
    email_alert = "#input-email+ .text-danger"
    password_alert = "#input-password+ .text-danger"
    password_confirm_alert = "#input-confirm + .text-danger"

    def click_and_clear_before_calling(locator_type, locator_value):
        def decorator(method):
            @wraps(method)
            def wrapper(self, *args, **kwargs):
                element = self.driver.find_element(locator_type, locator_value)
                element.click()
                element.clear()
                return method(self, *args, **kwargs)

            return wrapper

        return decorator

    @click_and_clear_before_calling(By.ID, firstname)
    def input_firstname(self, name):
        self.driver.find_element(By.ID, self.firstname).send_keys(name)
        return self

    @click_and_clear_before_calling(By.ID, lastname)
    def input_lastname(self, lastname):
        self.driver.find_element(By.ID, self.lastname).send_keys(lastname)
        return self

    def input_email(self, email):
        self.driver.find_element(By.ID, self.email).send_keys(email)
        return self

    def input_telephone(self, telephone):
        self.driver.find_element(By.ID, self.telephone).send_keys(telephone)
        return self

    def input_password(self, password):
        self.driver.find_element(By.ID, self.password).send_keys(password)
        return self

    def input_confirm_password(self, password):
        self.driver.find_element(By.ID, self.confirm_password).send_keys(password)
        return self

    def agree_privacy_policy(self):
        self.driver.find_element(By.NAME, self.agree_policy).click()
        return self

    def subscribe_newsletter(self):
        self.driver.find_element(By.CSS_SELECTOR, self.newsletter).click()
        return self

    def click_continue(self):
        self.driver.find_element(By.CSS_SELECTOR, self.next).click()
        return self

    def display_alert(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.alert)

    def get_first_name_alert(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.firstname_alert).text()

    def get_last_name_alert(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.lastname_alert).text()

    def get_email_alert(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.email_alert).text()

    def get_password_alert(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.password_alert).text()

    def get_password_confirmation_alert(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.password_confirm_alert).text()


factory = TestDataFactory()
test_data = factory.get_test_data('form')


