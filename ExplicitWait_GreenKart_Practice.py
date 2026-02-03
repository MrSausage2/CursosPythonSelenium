import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
expectedList= ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
driver.implicitly_wait(5)
time.sleep(2)

#Add items to cart
resultsList = driver.find_elements(By.XPATH, "//div[@class='products']/div")
actualProducts = driver.find_elements(By.CSS_SELECTOR, "h4.product-name")
count = len(resultsList)

for product in actualProducts:
    print(product.text)
    assert product.text == expectedList[actualProducts.index(product)]

assert count>0

for result in resultsList:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

#sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
itemsTotal = 0
for item in prices:
    itemsTotal+=int(item.text)

totalAmount = driver.find_element(By.CSS_SELECTOR, ".totAmt")
assert itemsTotal==int(totalAmount.text)

#ApplyCode
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
wait = WebDriverWait(driver, 10)
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait.until(expected_conditions.presence_of_element_located(
    (By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
print(itemsTotal)

totalWithDiscount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print(totalWithDiscount)
assert totalWithDiscount < itemsTotal