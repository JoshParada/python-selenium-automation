from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Verify there are {n} benefit cells')
def verify_cells(context, n):
    cell_count = len(context.driver.find_elements(By.CSS_SELECTOR, '.cell-item-content'))
    assert cell_count == int(n), f'Expected {n} benefit cells, got {cell_count}'