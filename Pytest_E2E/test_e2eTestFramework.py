import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pageObjects.ShopPage import ShopPage
from pageObjects.login import LoginPage


def test_e2e(browserInstance):
    driver=browserInstance
    wait_e2e = WebDriverWait(driver, 10)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    loginPage=LoginPage(driver)
    loginPage.login()

    shop_page=ShopPage(driver)
    phoneWanted = "Blackberry"
    shop_page.add_product_to_cart(phoneWanted)


    driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary").click()

    driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()

    driver.find_element(By.ID, "country").send_keys("me")

    WebDriverWait(driver, 10)
    countryCheck = "Armenia"
    wait_e2e.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, countryCheck)))

    driver.find_element(By.LINK_TEXT, countryCheck).click()
    driver.find_element(By.CSS_SELECTOR, ".checkbox.checkbox-primary").click()
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-success.btn-lg").click()

    successText = driver.find_element(By.CLASS_NAME, "alert-success").text
    assert "Success! Thank you!" in successText