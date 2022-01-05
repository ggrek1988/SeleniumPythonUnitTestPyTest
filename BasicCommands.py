from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)

driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)  # return Title of the page
print(driver.current_url)  # return url of the page
# print(driver.page_source)#return all page source
# driver.find_element_by_xpath("//button[@class='btn btn-info']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-info']").click()
time.sleep(5)
# driver.close() currently focussed browser
driver.quit()  # closes all browses
