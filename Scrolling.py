

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)

driver.get("https://www.flagi-panstw.pl/rejestr")

driver.maximize_window()
# 1 Scroll down page by poxel
#driver.execute_script("window.scrollBy(0,4000)","")

#2 Scroll down page till the element id visible
#flag = driver.find_elements_by_xpath("//img[@alt='Flaga Islandii']")
#driver.execute_script("arguments[0].scrollIntoView();",flag)

#3 scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")


