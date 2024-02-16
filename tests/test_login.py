import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_with_valid_credentials():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH,"//span[text()='My Account']").click()
    driver.find_element(By.XPATH,"//a[text()='Login']").click()
    driver.find_element(By.ID,"input-email").send_keys("amotooricap@gmail.com")
    driver.find_element(By.ID,"input-password").send_keys("12345")
    driver.find_element(By.CSS_SELECTOR,"input[type=submit].btn").click()
    assert driver.find_element(By.LINK_TEXT,)


