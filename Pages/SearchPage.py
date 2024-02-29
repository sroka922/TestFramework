from selenium.webdriver.common.by import By


class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    valid_hp_product = "HP LP3065"
    no_product_message_xpath = "//input[@id='button-search']/following-sibling::p"
    expected_text = "There is no product that matches the search criteria."

    def display_status_of_product(self):
        return self.driver.find_element(By.LINK_TEXT, self.valid_hp_product).is_displayed()

    def retrieve_no_products(self):
        return self.driver.find_element(By.XPATH, self.no_product_message_xpath).text
