import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


class AssertionTest1(unittest.TestCase):

    def test_Google(self):
        self.ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
        self.op = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(service=self.ser, options=self.op)

        self.driver.get("https://www.google.com/")

        titleOfWebPage = self.driver.title
        #self.assertEqual("Google123",titleOfWebPage,"webpage title is not same")
        self.assertNotEqual("Google123",titleOfWebPage)

if __name__ == "__main__":
    unittest.main()