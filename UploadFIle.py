from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)
driver.get("http://testautomationpractice.blogspot.com/")

driver.switch_to.frame(0)
driver.find_element(By.ID,"RESULT_FileUpload-10").send_keys("C://Capture001.png")