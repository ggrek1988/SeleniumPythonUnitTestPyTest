from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)

driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath("//button[@class='btn btn-info']").click()

print(driver.current_window_handle) #1cb21b0d-bb2a-4b67-baff-85993559e43c - parent

handles = driver.window_handles #return all the handle values of open browses windows

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close() #close only windows

time.sleep(3)
driver.quit()
