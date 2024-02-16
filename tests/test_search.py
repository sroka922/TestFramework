import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from datetime import datetime


def register_with_mandatory_fields():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH,"//span[text()='My Account']").click()
    driver.find_element(By.XPATH,"//a[text()='Register']").click()
    driver.implicitly_wait(2)
    driver.find_element(By.ID,"input-email").send_keys(generate_email_with_timestamp())
    driver.find_element(By.ID,"input-password").send_keys("12345")
    driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
    driver.implicitly_wait(2)
    alert = driver.find_element(By.CSS_SELECTOR,"div.alert")
    assert driver.find_element(By.CSS_SELECTOR,"div.alert").is_displayed()
    time.sleep(2)


def generate_email_with_timestamp():
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "amotoori"+time_stamp+"gmail.com"


    


