import time
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



@pytest.fixture()
def setup_and_teardown():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    yield
    driver.quit()


def test_register_with_mandatory_fields(setup_and_teardown):
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.XPATH, "//a[text()='Register']").click()
    driver.implicitly_wait(2)
    driver.find_element(By.ID, "input-firstname").send_keys("test")
    driver.find_element(By.ID, "input-lastname").send_keys("12345")
    driver.find_element(By.ID, "input-email").send_keys(generate_email_with_timestamp())
    driver.find_element(By.ID, "input-telephone").send_keys("123456789")
    driver.find_element(By.ID, "input-password").send_keys("12345")
    driver.find_element(By.ID, "input-confirm").send_keys("12345")
    driver.find_element(By.NAME, "agree").click()
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    assert driver.find_element(By.CSS_SELECTOR, "#content > h1").is_displayed()
    assert driver.find_element(By.CSS_SELECTOR, "#content > h1").text.__eq__("Your Account Has Been Created!")


def test_register_with_all_fields(setup_and_teardown):
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.XPATH, "//a[text()='Register']").click()
    driver.implicitly_wait(2)
    driver.find_element(By.ID, "input-firstname").send_keys("test")
    driver.find_element(By.ID, "input-lastname").send_keys("12345")
    driver.find_element(By.ID, "input-email").send_keys(generate_email_with_timestamp())
    driver.find_element(By.ID, "input-telephone").send_keys("123456789")
    driver.find_element(By.ID, "input-password").send_keys("12345")
    driver.find_element(By.ID, "input-confirm").send_keys("12345")
    driver.find_element(By.CSS_SELECTOR, "input[name='newsletter'][value='1']").click()
    driver.find_element(By.NAME, "agree").click()
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    assert driver.find_element(By.CSS_SELECTOR, "#content > h1").is_displayed()
    assert driver.find_element(By.CSS_SELECTOR, "#content > h1").text.__eq__("Your Account Has Been Created!")


def test_register_with_existing_email(setup_and_teardown):
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.XPATH, "//a[text()='Register']").click()
    driver.implicitly_wait(2)
    driver.find_element(By.ID, "input-firstname").send_keys("test")
    driver.find_element(By.ID, "input-lastname").send_keys("12345")
    driver.find_element(By.ID, "input-email").send_keys("amotooricap@gmail.com")
    driver.find_element(By.ID, "input-telephone").send_keys("123456789")
    driver.find_element(By.ID, "input-password").send_keys("12345")
    driver.find_element(By.ID, "input-confirm").send_keys("12345")
    driver.find_element(By.CSS_SELECTOR, "input[name='newsletter'][value='1']").click()
    driver.find_element(By.NAME, "agree").click()
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    assert driver.find_element(By.CSS_SELECTOR, ".alert-dismissible >i").is_displayed()
    assert (driver.find_element(By.CSS_SELECTOR, ".alert-dismissible")
            .text.__eq__("Warning: E-Mail Address is already registered!"))


def test_register_without_providing_any_data(setup_and_teardown):
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.XPATH, "//a[text()='Register']").click()
    driver.implicitly_wait(2)
    driver.find_element(By.ID, "input-firstname").send_keys("")
    driver.find_element(By.ID, "input-lastname").send_keys("")
    driver.find_element(By.ID, "input-email").send_keys("")
    driver.find_element(By.ID, "input-telephone").send_keys("")
    driver.find_element(By.ID, "input-password").send_keys("")
    driver.find_element(By.ID, "input-confirm").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "input[name='newsletter'][value='1']").click()
    driver.find_element(By.NAME, "agree").click()
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    assert (driver.find_element(By.CSS_SELECTOR, "#input-firstname  + .text-danger")
            .text.__eq__("First Name must be between 1 and 32 characters!"))
    assert (driver.find_element(By.CSS_SELECTOR, "#input-lastname+ .text-danger")
            .text.__eq__("Last Name must be between 1 and 32 characters!"))
    assert (driver.find_element(By.CSS_SELECTOR, "#input-email+ .text-danger")
            .text.__eq__("E-Mail Address does not appear to be valid!"))
    assert (driver.find_element(By.CSS_SELECTOR, "#input-password+ .text-danger")
            .text.__eq__("Password must be between 4 and 20 characters!"))


def test_register_with_bad_password_confirmation(setup_and_teardown):
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.XPATH, "//a[text()='Register']").click()
    driver.implicitly_wait(2)
    driver.find_element(By.ID, "input-firstname").send_keys("")
    driver.find_element(By.ID, "input-lastname").send_keys("")
    driver.find_element(By.ID, "input-email").send_keys("")
    driver.find_element(By.ID, "input-telephone").send_keys("")
    driver.find_element(By.ID, "input-password").send_keys("12345")
    driver.find_element(By.ID, "input-confirm").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "input[name='newsletter'][value='1']").click()
    driver.find_element(By.NAME, "agree").click()
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    assert (driver.find_element(By.CSS_SELECTOR, "#input-confirm + .text-danger")
            .text.__eq__("Password confirmation does not match password!"))


def generate_email_with_timestamp():
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "amotoori" + time_stamp + "@gmail.com"
