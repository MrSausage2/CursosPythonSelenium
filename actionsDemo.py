from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
action = ActionChains(driver)
#action.double_click(driver.find_element(By.))
#action.context_click(driver.find_element(By.)) <- click derecho

action.move_to_element(driver.find_element(By.ID, "mousehover")).perform() #se tiene que terminar con .perform() para que se ejecute la action
#action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()