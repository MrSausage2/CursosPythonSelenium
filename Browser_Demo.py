import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Chrome driver service. Selenium checa la versión de Chrome, descarga el driver de la versión y hace la conexión

#service_obj = Service(r"C:\Users\psanchez\Downloads\SeleniumTraining\ChromeDrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
#driver = webdriver.Chrome(service = service_obj)
#esto de arriba es cuando hay una VPN o algo que impida la conección. La descarga tiene que ser manual
#Lo mismo Para edge-> Edgedriver -> msedgedrive.exe
#Firefox-> Geckodriver ->geckodriver.exe

driver = webdriver.Edge()
driver.get("https://www.youtube.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(2) #Demostración visual de cómo abre y cierra el browser