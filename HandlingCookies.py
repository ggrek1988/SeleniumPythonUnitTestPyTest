from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)

driver.get("https://www.amazon.in")

cookies= driver.get_cookies()
print(len(cookies)) #pront number of cookies have ben created
print(cookies)

#Adding new cookie to the browser
cookie = {'name':'Mycookie','value':'1234567890'}
driver.add_cookie(cookie)

cookies= driver.get_cookies()
print(len(cookies)) #pront number of cookies have ben created
print(cookies)