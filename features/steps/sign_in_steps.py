from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Verify Sign In page')
def verify_sign_in_page(context):
    actual_result = context.driver.find_element(By.ID, "login").text
    expected_result = "Sign in with password"

    assert actual_result == expected_result, f'Expected {expected_result}, got {actual_result}'
    sleep(3)