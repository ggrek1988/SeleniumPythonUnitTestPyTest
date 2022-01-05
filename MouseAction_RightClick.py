from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)

driver.get("http://testautomationpractice.blogspot.com/")
button = driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")

actions = ActionChains(driver)
actions.context_click(button)