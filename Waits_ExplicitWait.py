from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)
driver.get("http://www.expedia.com")

driver.find_element(By.XPATH, "//span[normalize-space()='Flights']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@aria-label='Leaving from']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='location-field-leg1-origin']").send_keys("Londyn")

driver.find_element(By.XPATH, "//button[@aria-label='Going to']").click()
time.sleep(2)
input_city = driver.find_element(By.XPATH, "//input[@id='location-field-leg1-destination']")
input_city.send_keys("warszawa")
driver.find_element(By.CLASS_NAME(
    "uitk-layout-grid-item uitk-layout-grid-item-columnspan-medium-3 uitk-layout-grid-item-columnspan-large-5")).click()

time.sleep(5)
driver.find_element_by_xpath("//button[normalize-space()='Search']").click()
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Search']"))).click()
