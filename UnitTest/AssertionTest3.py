import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


class AssertionTest3(unittest.TestCase):

    def test_Google(self):
        self.ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
        self.op = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(service=self.ser, options=self.op)

        #driver1 = None
        #self.assertIsNone(driver1)

        self.assertIsNotNone(self.driver)



if __name__ == "__main__":
    unittest.main()