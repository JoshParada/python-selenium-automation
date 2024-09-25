from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class CartPage(Page):

    CART_EMPTY_TXT = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")
    CART_SUMMARY = (By.XPATH, "//*[contains(text(),'subtotal')]")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


    def verify_empty_cart(self):
        self.verify_text('Your cart is empty', *self.CART_EMPTY_TXT)
        sleep(3)

    def verify_item(self):
        self.verify_partial_text('subtotal', *self.CART_SUMMARY)
        sleep(3)

    def verify_product_name(self, context):
        self.verify_partial_text(context.product_name, *self.CART_ITEM_TITLE)
        sleep(3)
