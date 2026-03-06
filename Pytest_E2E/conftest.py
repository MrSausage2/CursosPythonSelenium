import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name=="chrome":
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.maximize_window()
    elif browser_name=="edge":
        driver = webdriver.Edge()
        driver.implicitly_wait(5)
        driver.maximize_window()
    yield driver
    driver.close() #el error se debía a que había un driver.close en el testcase