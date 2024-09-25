from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SearchResultsPage(Page):

    SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    FIRST_RESULT_ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[data-test="chooseOptionsButton"]')

    def verify_results(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULTS_HEADER)
        sleep(3)

    def verify_results_url(self, product):
        self.verify_partial_url(product)

    def add_first_item(self):
        self.wait_to_be_clickable_click(*self.FIRST_RESULT_ADD_TO_CART_BTN)