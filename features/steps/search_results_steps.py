from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


FIRST_RESULT_ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[data-test="chooseOptionsButton"]')
ADD_TO_CART_SIDEBAR_BTN = (By.CSS_SELECTOR, '[data-test="orderPickupButton"]')
CLOSE_SIDEBAR_BTN = (By.CSS_SELECTOR, '[type="button"][aria-label="close"]')
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")


@when('Add first item to cart')
def add_first_item(context):
    #click first item
    context.driver.wait.until(EC.element_to_be_clickable(FIRST_RESULT_ADD_TO_CART_BTN)).click()
    #add to cart
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_SIDEBAR_BTN)).click()
    #close side menu
    context.driver.wait.until(EC.element_to_be_clickable(CLOSE_SIDEBAR_BTN)).click()
    sleep(3)


@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print(f'Product stored: {context.product_name}')


@then('Verify that results match {item}')
def verify_search(context, item):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert item in actual_result, f'Expected {item}, got {actual_result}'
    sleep(3)