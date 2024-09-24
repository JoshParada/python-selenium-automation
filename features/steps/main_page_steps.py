from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target main page')
def target_page(context):
    context.app.main_page.open_main()

@given('Open Target Circle page')
def target_page(context):
    context.driver.get('https://target.com/circle')

