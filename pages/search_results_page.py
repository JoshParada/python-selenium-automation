from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SearchResultsPage(Page):

    SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    FIRST_RESULT_ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[data-test="chooseOptionsButton"]')
    HEART_ICON = (By.CSS_SELECTOR, "[data-test='FavoritesButton']")
    FAV_TOOLTIP = (By.XPATH, "//*[contains(text(), 'Click to sign in and save')]")

    def hover_favorites(self):
        heart_icon = self.find_element(*self.HEART_ICON)

        actions = ActionChains(self.driver)
        actions.move_to_element(heart_icon)
        actions.perform()
        sleep(3)

    def add_first_item(self):
        self.wait_to_be_clickable_click(*self.FIRST_RESULT_ADD_TO_CART_BTN)

    def verify_favorites(self):
        self.wait_for_element_to_appear(*self.FAV_TOOLTIP)

    def verify_results(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULTS_HEADER)
        sleep(3)

    def verify_results_url(self, product):
        self.verify_partial_url(product)

