from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@then('Verify cart is empty')
def verify_empty_cart(context):
    context.app.cart_page.verify_empty_cart()

@then('Verify item is in cart')
def verify_item(context):
    context.app.cart_page.verify_item()


@then('Verify cart has correct product')
def verify_product_name(context):
    context.app.cart_page.verify_product_name(context)
