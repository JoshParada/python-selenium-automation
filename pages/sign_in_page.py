from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class Sign_In_Page(Page):

    SIGN_IN_BTN = (By.ID, "login")

    def verify_sign_in_page(self):
        self.verify_text("Sign in with password", *self.SIGN_IN_BTN)