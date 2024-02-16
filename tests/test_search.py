import datetime
import time

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

def test_search_for_a_valid_product(setup_and_teardown):
    driver.find_element(By.NAME, "search").send_keys("HP")
    driver.find_element(By.CSS_SELECTOR, "button.btn-default").click()
    assert driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()

def test_search_for_a_invalid_product(setup_and_teardown):
    driver.find_element(By.NAME, "search").send_keys("Honda")
    driver.find_element(By.CSS_SELECTOR, "button.btn-default").click()
    expected_text = "There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)

def test_search_without_entering_any_product(setup_and_teardown):
    driver.find_element(By.CSS_SELECTOR, 'button.btn-default').click()
    expected_text = "There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)


def test_go_to_Desktop(setup_and_teardown):
    driver.find_element(By.CSS_SELECTOR, 'ul.nav > li:first-of-type').click()
    assert driver.find_element(By.CSS_SELECTOR, 'li.dropdown.open > a:first-of-type').is_displayed()
    driver.implicitly_wait(2)






