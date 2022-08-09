# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import logging

print('Starting the browser...')
# options = ChromeOptions()
# options.add_argument("--headless")
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


# Start the browser and login with standard_user
def login(user, password):
    print('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')

    print('Trying to login a user {}'.format(user))
    driver.find_element(
        By.CSS_SELECTOR, "input[id='user-name']").send_keys(user)
    driver.find_element(
        By.CSS_SELECTOR, "input[id='password']").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "input[id='login-button']").click()

    products_title = driver.find_element(
        By.CSS_SELECTOR, "div[id='header_container'] > div > span.title").text
    if "PRODUCTS" in products_title:
        logging.info("Login successfully. Navigating to the demo page to products")
    else:
        logging.info('ERROR! when login you in!')


def add_products():
    title_products = driver.find_elements(
        By.CSS_SELECTOR, "div[class='inventory_item_name']")
    for title in title_products:
        logging.info('Adding product {}'.format(title.text))
    buttons_add_to_cart = driver.find_elements(
        By.CSS_SELECTOR, "button[class='btn btn_primary btn_small btn_inventory']")
    for button in buttons_add_to_cart:
        button.click()

    logging.info('Successfully added all products')

    for title in title_products:
        logging.info('Removing product {}'.format(title.text))
    buttons_remove_from_cart = driver.find_elements(
        By.CSS_SELECTOR, "button[class='btn btn_secondary btn_small btn_inventory']")
    for button in buttons_remove_from_cart:
        button.click()

    logging.info('Successfully removed all products')


login('standard_user', 'secret_sauce')
add_products()