import json

from selenium.webdriver.common.by import By
from functools import wraps

from Pages.LoginPage import LoginPage
from Pages.SearchPage import SearchPage


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

    def click_and_clear_before_calling(locator_type, locator_value):
        def decorator(method):
            @wraps(method)
            def wrapper(self, *args, **kwargs):
                element = self.driver.find_element(locator_type, locator_value)
                element.click().clear()
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


def load_credentials_from_json(filename='credentials.json'):
    with open(filename, 'r') as file:
        data = json.load(file)
    return [(user['email'], user['password']) for user in data['Credentials']]


def loadJson(filename='test'):
    with open(filename, 'r') as file:
        data = json.load(file)
    return [(user['email'], user['password']) for user in data['Credentials']]


credentials_path = 'C:\\Users\\kryst\\PycharmProjects\\TestFramework\\configurations\\Credentials.json'
credentials_data = load_credentials_from_json(credentials_path)