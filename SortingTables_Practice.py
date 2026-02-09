from selenium import webdriver
from selenium.webdriver.common.by import By

browserSortedVeggies = []
driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
veggieWebElements=driver.find_elements(By.XPATH, "//tr/td[1]")

for veggie in veggieWebElements:
    browserSortedVeggies.append(veggie.text)

print(browserSortedVeggies)
originalBrowserSortedVeggies=browserSortedVeggies.copy()

browserSortedVeggies.sort()
assert originalBrowserSortedVeggies == browserSortedVeggies

