from selenium.webdriver.common.by import By

from Pages.LoginPage import LoginPage
from Pages.SearchPage import SearchPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    search_box_field_name = "search"
    search_button = "button.btn-default"
    my_account_dropbown_menu = "//span[text()='My Account']"
    my_account = "//span[text()='My Account']"
    login = "//a[text()='Login']"

    def enter_product_into_search_box_field(self, product_name):
        self.driver.find_element(By.NAME, self.search_box_field_name).click()
        self.driver.find_element(By.NAME, self.search_box_field_name).clear()
        self.driver.find_element(By.NAME, self.search_box_field_name).send_keys(product_name)
        return self

    def click_search_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.search_button).click()
        return self

    def click_on_account_dropdown_menu(self):
        self.driver.find_element(By.XPATH,self.my_account_dropbown_menu).click()
        return self

    def click_on_MyAccount(self):
        self.driver.find_element(By.XPATH,self.my_account).click()
        return self

    def click_on_Login(self):
        self.driver.find_element(By.XPATH,self.login).click()
        return self



