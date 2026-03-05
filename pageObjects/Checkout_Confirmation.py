from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Checkout_Confirmation:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.CSS_SELECTOR, ".btn.btn-success")
        self.country_input = (By.ID, "country")
        self.checkbox=(By.CSS_SELECTOR, ".checkbox.checkbox-primary")
        self.submit_button = (By.CSS_SELECTOR, ".btn.btn-success.btn-lg")
        self.success_message = (By.CLASS_NAME, "alert-success")



    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def country_delivery(self,countryName):
        self.driver.find_element(*self.country_input).send_keys("me")

        wait=WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, countryName)))

        self.driver.find_element(By.LINK_TEXT, countryName).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit_button).click()


    def validate_order(self):
        successText = self.driver.find_element(*self.success_message).text
        assert "Success! Thank you!" in successText