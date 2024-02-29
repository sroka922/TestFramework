from lib2to3.pgen2 import driver

import pytest
from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from Pages.SearchPage import SearchPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_a_valid_product(self):
        HomePage(self.driver) \
            .enter_product_into_search_box_field("HP") \
            .click_search_button()
        search_page = SearchPage(self.driver)
        assert search_page.display_status_of_product()


    def test_search_for_a_invalid_product(self):
        HomePage(self.driver) \
            .enter_product_into_search_box_field("Honda") \
            .click_search_button()
        search_page = SearchPage(self.driver)
        assert search_page.retrieve_no_products().__eq__(search_page.expected_text)

    def test_search_without_entering_any_product(self):
        HomePage(self.driver) \
            .click_search_button()
        search_page = SearchPage(self.driver)
        assert search_page.retrieve_no_products().__eq__(search_page.expected_text)
    def test_go_to_Desktop(self):
        self.driver.find_element(By.CSS_SELECTOR, 'ul.nav > li:first-of-type').click()
        assert self.driver.find_element(By.CSS_SELECTOR, 'li.dropdown.open > a:first-of-type').is_displayed()
        self.driver.implicitly_wait(2)
