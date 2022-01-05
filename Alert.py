from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)

driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("//button[@onclick='myFunction()']").click()
time.sleep(5)

# driver.switch_to.alert.accept() #closes alert windows using OK button

driver.switch_to.alert.dismiss()  # close alert windows using cancel buton
