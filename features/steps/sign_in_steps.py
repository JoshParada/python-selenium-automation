from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on Target terms and conditions link')
def go_to_terms_and_conditions(context):
    context.app.sign_in_page.go_to_terms_and_conditions()

@then('Verify Sign In page')
def verify_sign_in_page(context):
    context.app.sign_in_page.verify_sign_in_page()

@then('Verify Terms and Conditions page is opened')
def verify_tac_opened(context):
    context.app.sign_in_page.verify_tac_opened()
