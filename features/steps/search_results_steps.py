from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Add first item to cart')
def add_first_item(context):
    sleep(5)
    #click first item
    context.driver.find_elements(By.CSS_SELECTOR, '[data-test="chooseOptionsButton"]')[0].click()
    sleep(5)
    #add to cart
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="orderPickupButton"]').click()
    sleep(5)
    #close side menu
    context.driver.find_elements(By.CSS_SELECTOR, '[type="button"][aria-label="close"]')[1].click()
    sleep(3)


@then('Verify that results match {item}')
def verify_search(context, item):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert item in actual_result, f'Expected {item}, got {actual_result}'
    sleep(2)