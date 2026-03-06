class BrowserUtils:
    def __init__(self, driver):
        self.driver=driver

    def getpagetitle(self):
        return self.driver.title