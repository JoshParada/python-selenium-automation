from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_SUMMARY = (By.XPATH, "//*[contains(text(),'subtotal')]")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@then('Verify cart is empty')
def verify_empty_cart(context):
    context.app.cart_page.verify_empty_cart()

@then('Verify item is in cart')
def verify_item(context):
    actual_result = context.driver.find_element(*CART_SUMMARY).text
    assert 'subtotal' in actual_result, f'Expected subtotal, got {actual_result}'
    sleep(3)


@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    print(f'Actual product in cart name: {actual_name}')
    assert context.product_name in actual_name, f"Expected {context.product_name} but got {actual_name}"