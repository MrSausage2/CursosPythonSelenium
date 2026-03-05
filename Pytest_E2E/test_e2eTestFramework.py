import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pageObjects.login import LoginPage
from pageObjects.ShopPage import ShopPage


def test_e2e(browserInstance):
    driver=browserInstance
    wait_e2e = WebDriverWait(driver, 10)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    loginPage = LoginPage(driver)
    shop_page = loginPage.login()


    #itemWanted = "Blackberry"
    shop_page.add_product_to_cart("Blackberry")
    checkout_confirmation = shop_page.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.country_delivery()
    checkout_confirmation.validate_order()






