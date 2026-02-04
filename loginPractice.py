from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
wait = WebDriverWait(driver, 15)
driver.implicitly_wait(5)

driver.find_element(By.CLASS_NAME, "blinkingText").click()

windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
testEmai = driver.find_element(By.CSS_SELECTOR, "a[href='mailto:mentor@rahulshettyacademy.com']").text

driver.switch_to.window(windowsOpened[0])

driver.find_element(By.CSS_SELECTOR, "#username").send_keys(testEmai)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("pluh123")
driver.find_element(By.XPATH, "(//span[@class='checkmark'])[2]").click()
driver.find_element(By.CSS_SELECTOR, "#okayBtn").click()

driver.find_element(By.CSS_SELECTOR, "select[data-style=btn-info]").click()
driver.find_element(By.CSS_SELECTOR, "option[value=teach]").click()
driver.find_element(By.CSS_SELECTOR, "#terms").click()
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()


print((wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert.alert-danger.col-md-12")))).text)
#driver.find_element(By.CLASS_NAME, "alert.alert-danger.col-md-12")

print(driver.title)
print(testEmai)

