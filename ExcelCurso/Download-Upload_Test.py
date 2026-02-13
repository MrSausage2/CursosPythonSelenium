from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

file_path= r"C:\Users\psanchez\Downloads\download.xlsx"
driver = webdriver.Chrome()

driver.implicitly_wait(6)
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")

driver.find_element(By.ID, "downloadButton").click()

file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys(file_path)
toast_locator=(By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")
WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(toast_locator))

print(driver.find_element(*toast_locator).text)