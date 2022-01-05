import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

class SearchEngineTest(unittest.TestCase):
    
    def test_Google(self):
        self.ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
        self.op = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(service=self.ser, options=self.op)

        self.driver.get("https://www.google.com/")
        print("This of the page is: "+self.driver.title)
        self.driver.close()

    def test_Bing(self):
        self.ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
        self.op = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(service=self.ser, options=self.op)

        self.driver.get("https://www.bing.com")
        print("This of the page is: "+self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
