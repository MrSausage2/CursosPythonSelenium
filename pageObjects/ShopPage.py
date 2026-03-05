from selenium.webdriver.common.by import By

from CursosPythonSelenium.pageObjects.Checkout_Confirmation import Checkout_Confirmation


class ShopPage:
    def __init__(self,driver):
        self.driver = driver
        self.shop_link = (By.CSS_SELECTOR, "a[href*=shop]")
        self.phone_cards = (By.XPATH, "//div[@class='card h-100']")
        self.checkout_button = (By.CSS_SELECTOR, ".nav-link.btn.btn-primary")

    def add_product_to_cart(self, phoneWanted):
        self.driver.find_element(*self.shop_link).click()
        productName=phoneWanted
        windowsOpened = self.driver.window_handles

        phoneCards = self.driver.find_elements(self.phone_cards)

        self.driver.switch_to.window(windowsOpened[0])

        for card in phoneCards:
            if productName == card.find_element(By.XPATH, "div/h4/a").text:
                # print(card.find_element(By.XPATH, "div/h4/a").text)
                card.find_element(By.XPATH, "div/button").click()

    def goToCart(self):
        self.driver.find_element(*self.checkout_button).click()
        checkout_confirmation=Checkout_Confirmation(self.driver)
        return checkout_confirmation