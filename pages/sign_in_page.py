from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class Sign_In_Page(Page):

    SIGN_IN_BTN = (By.ID, "login")
    TERMS_AND_CONDITIONS = (By.XPATH, "//a[contains(text(),'terms')]")


    def go_to_terms_and_conditions(self):
        self.wait_to_be_clickable_click(*self.TERMS_AND_CONDITIONS)

    def verify_sign_in_page(self):
        self.verify_text("Sign in with password", *self.SIGN_IN_BTN)

    def verify_tac_opened(self):
        self.verify_partial_url('terms-conditions')