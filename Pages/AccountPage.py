from lib2to3.pgen2 import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AccountPage:

    def __init__(self, driver):
        self.driver = driver

    edit_your_account_information_option_text = "Edit your account information"
    accountInfo = "#content a[href*='account/edit']"
    lackEmail = ".alert > i.fa"

    def myAccount(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.accountInfo).text

    def wait_until_page_loaded(self):
        (WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.accountInfo))))

    def myAccountInfo(self):
        self.wait_until_page_loaded()
        return self.driver.find_element(By.CSS_SELECTOR, self.lackEmail).is_displayed()

