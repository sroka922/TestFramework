import datetime
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from datetime import datetime


@pytest.fixture()
def setup_and_teardown():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    yield
    driver.quit()

def test_login_with_valid_credentials(setup_and_teardown):
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.XPATH, "//a[text()='Login']").click()
    driver.find_element(By.ID, "input-email").send_keys("amotooricap@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("12345")
    driver.find_element(By.CSS_SELECTOR, "input[type=submit].btn").click()
    assert (driver.find_element(By.CSS_SELECTOR, "#content a[href*='account/edit']")
            .text.__eq__("Edit your account information"))


def test_login_with_invalid_credentials(setup_and_teardown):
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
    driver.implicitly_wait(2)
    driver.find_element(By.ID, "input-email").send_keys(generate_email_with_timestamp())
    driver.find_element(By.ID, "input-password").send_keys("12345")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    driver.implicitly_wait(2)
    alert = driver.find_element(By.CSS_SELECTOR, "div.alert")
    assert driver.find_element(By.CSS_SELECTOR, "div.alert").is_displayed()
    time.sleep(2)


def test_login_without_any_credentials(setup_and_teardown):
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.XPATH, "//a[text()='Login']").click()
    driver.find_element(By.CSS_SELECTOR, "input[type=submit].btn").click()
    res = driver.find_element(By.CSS_SELECTOR, ".alert-dismissible").text
    assert (driver.find_element(By.CSS_SELECTOR, ".alert-dismissible")
            .text.__eq__("Warning: No match for E-Mail Address and/or Password."))


def generate_email_with_timestamp():
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "amotoori" + time_stamp + "@gmail.com"
