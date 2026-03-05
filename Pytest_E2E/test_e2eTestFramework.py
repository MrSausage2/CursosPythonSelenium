import json
import sys
import os

import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pageObjects.login import LoginPage

test_data_path = "../Data/test_e2eTestFramework.json"
with open(test_data_path) as f:
    testData = json.load(f)
    testListData = testData["data"]

@pytest.mark.parametrize("testListItem", testListData)
def test_e2e(browserInstance, testListItem):
    driver=browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    loginPage = LoginPage(driver)
    shop_page = loginPage.login(testListItem["userEmail"], testListItem["userPassword"])
    itemWanted = testListItem["productName"]
    shop_page.add_product_to_cart(itemWanted)

    checkout_confirmation = shop_page.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.country_delivery(testListItem["countryDelivery"])
    checkout_confirmation.validate_order()

#py.test test_e2eTestFramework.py --browser_name chrome -s -v





