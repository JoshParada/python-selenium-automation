from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class CartPage(Page):
    def verify_empty_cart(self):
        actual_result = self.find_element(By.CSS_SELECTOR, "div[data-test='boxEmptyMsg'] h1").text
        expected_result = "Your cart is empty"
        assert actual_result == expected_result, f'Expected {expected_result}, got {actual_result}'
        sleep(3)