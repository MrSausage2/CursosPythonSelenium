from selenium.webdriver.common.by import By
from pageObjects.ShopPage import ShopPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input=(By.ID, "username")
        self.password=(By.NAME, "password")
        self.signIN=(By.ID, "signInBtn")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.signIN).click()
        shop_page = ShopPage(self.driver)
        return shop_page
    #