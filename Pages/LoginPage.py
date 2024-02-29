from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email = "input-email"
    password = "input-password"
    submit = "input[type=submit].btn"
    accountInfo = "#content a[href*='account/edit']"

    def input_login(self, login):
        self.driver.find_element(By.ID, self.email).send_keys(login)
        return self

    def input_password(self, password):
        self.driver.find_element(By.ID, self.password).send_keys(password)
        return self

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, self.submit).click()
        return self

    def myAccount(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.accountInfo).text
