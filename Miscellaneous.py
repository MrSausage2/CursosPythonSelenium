from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0,500);")
#Lo de arriba es para inyectar codigo javascript a traves de Selenium
#Es muy comun que el scroll se use para la automatizacion

driver.get_screenshot_as_file("sc_test.png")
