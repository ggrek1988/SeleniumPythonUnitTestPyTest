import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


class AssertionTest(unittest.TestCase):

    def testName(self):
        self.assertLessEqual(100,100)
        #self.assertLess(10,100)

        #self.assertGreater(100,10)
        #self.assertGreaterEqual(100,10)


if __name__ == "__main__":
    unittest.main()
