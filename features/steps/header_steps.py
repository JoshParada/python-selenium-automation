from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Go to Cart')
def cart_page(context):
    context.app.header.go_to_cart()


@when('Search for {item}')
def search_page(context, item):
    context.app.header.search_product(item)


@when('Go to Sign In')
def sign_in(context):
    context.app.header.sign_in()


@when('Add to cart via sidebar')
def add_to_cart(context):
    # add to cart
    context.app.header.add_to_cart()
    # close side menu
    context.app.header.close_sidebar()
    sleep(3)