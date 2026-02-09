from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options= webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

#programcreek.con/python/example/100025/selenium.webdriver.ChromeOptions
driver = webdriver.Chrome(options=chrome_options)#siempre pasar las options para que se ejecuten al invocar el browser
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")