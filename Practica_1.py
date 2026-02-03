import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")

driver.find_element(By.CSS_SELECTOR, ".forgot-password-link").click()
time.sleep(6)
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("dellazyr@mail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("zury2001")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("zury2001")
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("me")
time.sleep(2)
paises = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")


for pais in paises:
    if pais.text == "Mexico":
        pais.click()
        break
if driver.find_element(By.ID,"autosuggest").get_attribute("value") == "Mexico":
    driver.find_element(By.ID, "ctl00_mainContent_rbtnl_Trip_1").click()
    driver.find_element(By.ID, "ctl00_mainContent_ddl_originStation1_CTXT").send_keys("b")
    print("Error 4")

time.sleep(6)




