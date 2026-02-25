from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, "a[href*=shop]").click()

windowsOpened = driver.window_handles
phoneWanted = "Blackberry"
phoneCards = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

driver.switch_to.window(windowsOpened[0])

for card in phoneCards:
    if phoneWanted == card.find_element(By.XPATH, "div/h4/a").text:
        #print(card.find_element(By.XPATH, "div/h4/a").text)
        card.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary").click()

driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()

driver.find_element(By.ID, "country").send_keys("me")

WebDriverWait(driver, 10)
countryCheck = "Armenia"
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, countryCheck)))

driver.find_element(By.LINK_TEXT, countryCheck).click()
driver.find_element(By.CSS_SELECTOR, ".checkbox.checkbox-primary").click()
driver.find_element(By.CSS_SELECTOR, ".btn.btn-success.btn-lg").click()

successText = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success! Thank you!" in successText

driver.close()
