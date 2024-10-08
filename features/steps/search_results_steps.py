from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


FIRST_RESULT_ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[data-test="chooseOptionsButton"]')
ADD_TO_CART_SIDEBAR_BTN = (By.CSS_SELECTOR, '[data-test="orderPickupButton"]')
CLOSE_SIDEBAR_BTN = (By.CSS_SELECTOR, '[type="button"][aria-label="close"]')
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')


@when('Add first item to cart')
def add_first_item(context):
    context.app.search_results_page.add_first_item()


@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print(f'Product stored: {context.product_name}')

@when('Hover favorites icon')
def hover_favorites(context):
    context.app.search_results_page.hover_favorites()


@then('Favorites tooltip is shown')
def verify_favorites(context):
    context.app.search_results_page.verify_favorites()


@then('Verify that results match {item}')
def verify_results(context, item):
    context.app.search_results_page.verify_results(item)


@then('Verify product {product} in URL')
def verify_results_url(context, product):
    context.app.search_results_page.verify_results_url(product)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    all_products = context.driver.find_elements(*LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4]

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(title)
        product.find_element(*PRODUCT_IMG)