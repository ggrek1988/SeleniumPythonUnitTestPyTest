from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)

driver.get("https://www.amazon.in")

#driver.save_screenshot("C:\sss\homepage.png")

driver.get_screenshot_as_file("C:\sss\homepage1.png")