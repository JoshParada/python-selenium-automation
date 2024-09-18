from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify cart is empty')
def verify_cart(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "div[data-test='boxEmptyMsg'] h1").text
    expected_result = "Your cart is empty"
    assert actual_result == expected_result, f'Expected {expected_result}, got {actual_result}'
    sleep(3)


@then('Verify item is in cart')
def verify_item(context):
    actual_result = context.driver.find_element(By.XPATH, "//*[contains(text(),'subtotal')]").text
    assert 'subtotal' in actual_result, f'Expected subtotal, got {actual_result}'
    sleep(3)