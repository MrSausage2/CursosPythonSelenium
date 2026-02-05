from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/iframe")
driver.find_element(By.CSS_SELECTOR, ".tox-notification__dismiss.tox-button.tox-button--naked.tox-button--icon").click()


driver.get("https://demo.automationtesting.in/Frames.html")
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[0])


driver.switch_to.frame("singleframe")#tenemos que switch al embeded frame

driver.find_element(By.CSS_SELECTOR, "input[type=text]").send_keys("Della Zyr")

print(driver.find_element(By.CSS_SELECTOR, "input[type=text]").text)
#driver.find_element(By.ID, "tinymce").send_keys("Automation of frames")

