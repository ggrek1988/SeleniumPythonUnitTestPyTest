from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)

driver.get("file:///C:/Users/ggrek/Desktop/python/strona.html")

row = len(driver.find_element_by_xpath("/html/body/table/tbody/tr"))
cols = len(driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/th"))

print(row)
print(cols)
print("Heading 1" + "    " + "Heading 2")
for i in range(2, row + 1):
    for c in range(1, cols + 1):
        value = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[" + str(i) + "]/td[" + str(c) + "]").text

        print(value, end='    ')

    print()
