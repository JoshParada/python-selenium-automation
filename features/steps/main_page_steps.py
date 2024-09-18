from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target main page')
def target_page(context):
    context.driver.get('https://target.com')


@given('Open Target Circle page')
def target_page(context):
    context.driver.get('https://target.com/circle')


@when('Go to Sign In')
def sign_in_page(context):
    # click sign in button
    context.driver.find_element(By.XPATH, "//*[text()='Sign in']").click()
    # click sign in button from sidebar
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()


@when('Go to Cart')
def cart_page(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/CartLink']").click()
    sleep(3)


@when('Search for {item}')
def search_page(context, item):
    context.driver.find_element(By.ID, 'search').send_keys(item)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
    sleep(3)