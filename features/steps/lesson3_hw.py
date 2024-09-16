from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#--------------------------------PART 1----------------------------------------------
#amazon logo
#driver.find_element(By.CSS_SELECTOR, "a-icon.a-icon-logo")

#create account text
#driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

#your name input
#driver.find_element(By.ID, "ap_customer_name")

#email input
#driver.find_element(By.ID, "ap_email")

#password input
#driver.find_element(By.ID, "a-icon.a-ap_password-logo")

#password 6 char
#driver.find_element(By.ID, "auth-password-missing-alert")

#re-enter password field
#driver.find_element(By.ID, "ap_password_check")

#create your amazon account button
#driver.find_element(By.ID, "continue")

#condidtions of use link
#driver.find_element(By.CSS_SELECTOR, "[href*="condition_of_use"]")

#privacy notice link
#driver.find_element(By.CSS_SELECTOR, "[href*="privacy_notice"]")

#sign in link
#driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")



#--------------------------------PART 2----------------------------------------------

@given('Open Target main page')
def target_page(context):
    context.driver.get('https://target.com')

@when('Go to Cart')
def cart_page(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/CartLink']").click()

@then('Verify cart is empty')
def verify_cart(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "div[data-test='boxEmptyMsg'] h1").text
    expected_result = "Your cart is empty"

    assert actual_result == expected_result, f'Expected {expected_result}, got {actual_result}'
    sleep(3)

#------------------------------------PART 3-----------------------------------------

@when('Go to Sign In')
def sign_in_page(context):
    # click sign in button
    context.driver.find_element(By.XPATH, "//*[text()='Sign in']").click()
    # click sign in button from sidebar
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()


@then('Verify Sign In page')
def verify_sign_in_page(context):
    actual_result = context.driver.find_element(By.ID, "login").text
    expected_result = "Sign in with password"

    assert actual_result == expected_result, f'Expected {expected_result}, got {actual_result}'
    sleep(3)