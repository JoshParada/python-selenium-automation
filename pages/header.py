from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_BTN = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")
    SIGN_IN_BTN = (By.XPATH, "//*[text()='Sign in']")

    SIGN_IN_BTN_SIDEBAR = (By.XPATH, "//a[@data-test='accountNav-signIn']")
    ADD_TO_CART_SIDEBAR_BTN = (By.CSS_SELECTOR, '[data-test="orderPickupButton"]')
    CLOSE_SIDEBAR_BTN = (By.CSS_SELECTOR, '[type="button"][aria-label="close"]')

    def search_product(self, item):
        self.input_text(item, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(8)

    def go_to_cart(self):
        self.wait_to_be_clickable_click(*self.CART_BTN)
        sleep(3)

    def sign_in(self):
        # click sign in button
        self.find_element(*self.SIGN_IN_BTN).click()
        # click sign in button from sidebar
        self.wait_to_be_clickable_click(*self.SIGN_IN_BTN_SIDEBAR)
        sleep(3)

    def add_to_cart(self):
        self.find_element(*self.ADD_TO_CART_SIDEBAR_BTN).click()

    def close_sidebar(self):
        self.find_element(*self.CLOSE_SIDEBAR_BTN).click()