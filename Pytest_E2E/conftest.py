import os
import pytest
from selenium import webdriver
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
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

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), 'Reports')
            file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_") + ".png")
            print("file name is " + file_name)
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extras = extra

def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)