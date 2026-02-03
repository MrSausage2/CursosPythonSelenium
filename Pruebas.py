from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://jobs.jobvite.com/amberstudiocareers/")

# Opción 1: Esperar explícitamente con WebDriverWait (RECOMENDADO)
wait = WebDriverWait(driver, 10)
locations = wait.until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "//a[contains(@class, 'jv-button') and contains(@class, 'jv-button--hollow')]")
    )
)
print(f"Encontrados: {len(locations)}")

for location in locations:
    print(location.text)
    if location.text == "Guadalajara Careers":
        print("Guadalajara Careers")
        location.click()
        break