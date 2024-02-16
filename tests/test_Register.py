import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from datetime import datetime


def test_search_for_a_valid_product():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.NAME, "search").send_keys("HP")
    driver.find_element(By.CSS_SELECTOR, "button.btn-default").click()
    assert driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
    driver.quit()


def test_search_for_a_invalid_product():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.NAME, "search").send_keys("Honda")
    driver.find_element(By.CSS_SELECTOR, "button.btn-default").click()
    expected_text = "There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)
    driver.quit()


def test_search_without_entering_any_product():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.CSS_SELECTOR, 'button.btn-default').click()
    expected_text = "There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)
    driver.quit()


def test_go_to_Desktop():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.CSS_SELECTOR, 'ul.nav > li:first-of-type').click()
    assert driver.find_element(By.CSS_SELECTOR, 'li.dropdown.open > a:first-of-type').is_displayed()
    driver.implicitly_wait(2)


def test_login_with_valid_credentials():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
    driver.implicitly_wait(2)
    driver.find_element(By.ID, "input-email").send_keys("amotooricap@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("12345")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    driver.implicitly_wait(2)
    assert driver.find_element(By.CSS_SELECTOR, "#content a[href*='account/edit']").is_displayed()
    time.sleep(2)


def test_login_with_valid_credentials():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
    driver.implicitly_wait(2)
    driver.find_element(By.ID, "input-email").send_keys("amotooricap@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("12345")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    driver.implicitly_wait(2)
    assert driver.find_element(By.CSS_SELECTOR, "#content a[href*='account/edit']").is_displayed()
    time.sleep(2)


def test_login_with_invalid_credentials():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
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


def generate_email_with_timestamp():
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "amotoori" + time_stamp + "gmail.com"





