from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Go to Cart')
def cart_page(context):
    context.app.header.go_to_cart()


@when('Search for {item}')
def search_page(context, item):
    context.app.header.search_product(item)
