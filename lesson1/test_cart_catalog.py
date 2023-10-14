from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    # time.sleep(3)
    item = driver.find_element(By.XPATH, "//*[contains(text(),'Sauce Labs Backpack')]")

    cart_field = driver.find_element(By.XPATH, '//*[@data-test="add-to-cart-sauce-labs-backpack"]')
    cart_field.click()

    # time.sleep(3)

    cart = driver.find_element(By.XPATH, '// *[ @class ="shopping_cart_link"]')
    cart.click()

    # time.sleep(3)
    assert item
