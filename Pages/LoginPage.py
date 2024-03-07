from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Pages.AccountPage import AccountPage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email = "input-email"
    password = "input-password"
    submit = "input[type=submit].btn"
    accountInfo = "#content a[href*='account/edit']"
    passwordInfo = "12345"
    lackData = ".alert-dismissible"

    def input_login(self, login):
        self.driver.find_element(By.ID, self.email).click()
        self.driver.find_element(By.ID, self.email).clear()
        self.driver.find_element(By.ID, self.email).send_keys(login)
        return self

    def input_password(self, password):
        self.driver.find_element(By.ID, self.password).click()
        self.driver.find_element(By.ID, self.password).clear()
        self.driver.find_element(By.ID, self.password).send_keys(password)
        return self

    def input_wrong_password(self):
        self.driver.find_element(By.ID, self.password).click()
        self.driver.find_element(By.ID, self.password).clear()
        self.driver.find_element(By.ID, self.password).send_keys("test")
        return self

    def input_Empty_password(self):
        self.driver.find_element(By.ID, self.password).click()
        self.driver.find_element(By.ID, self.password).clear()
        self.driver.find_element(By.ID, self.password).send_keys("")
        return self

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, self.submit).click()
        wait = WebDriverWait(self.driver, 10)
        login_page = wait.until(EC.visibility_of_element_located((By.ID, self.email)))
        return self

    def lack_of_credentials(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.lackData).text
