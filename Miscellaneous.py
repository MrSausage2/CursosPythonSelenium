from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")#Ejecutar la prueba sin imagen
chrome_options.add_argument("--ignore-certificate-errors")
#Lo de arriba es para ignorar/pasar/cerrar las ventanas de advertencia
#Por ejemplo conexión no segura o error de certificado

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0,500);")
#Lo de arriba es para inyectar codigo javascript a traves de Selenium
#Es muy comun que el scroll se use para pruebas de automatizacion

driver.get_screenshot_as_file("sc_test.png")
