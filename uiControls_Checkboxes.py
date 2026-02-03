import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
   if checkbox.get_attribute("value") =="option2":
       checkbox.click()
       assert checkbox.is_selected()
       break

radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons[1].click()

assert radiobuttons[1].is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed() #assert not == false

driver.find_element(By.ID, "name").send_keys("Pablo")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
alert.accept()

driver.find_element(By.ID, "confirmbtn").click()

time.sleep(3)