from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)

driver.get("http://www.python.org")

print(driver.title)  # return Title of the page
print(driver.current_url)  # return url of the page

# print(driver.page_source)#return all page source
driver.close()
