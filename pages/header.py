from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_BTN = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")

    def search_product(self, item):
        self.input_text(item, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)

    def go_to_cart(self):
        self.find_element(*self.CART_BTN).click()
        sleep(3)


    def sign_in(self):
        # click sign in button
        self.find_element(By.XPATH, "//*[text()='Sign in']").click()
        # click sign in button from sidebar
        self.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
