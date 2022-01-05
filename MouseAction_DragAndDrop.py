from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)

driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

source_element = driver.find_element(By.XPATH,"//*[@id='box7']")
target_element = source_element = driver.find_element(By.XPATH,"//*[@id='box106']")

actions = ActionChains(driver)
actions.drag_and_drop(source_element,target_element).perform()