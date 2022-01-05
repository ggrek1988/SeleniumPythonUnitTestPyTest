from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

admin = driver.find_element(By.XPATH, "//*[@id='menu_admin_viewAdminModule']")
usermgnt = driver.find_element(By.XPATH, "//*[@id='menu_admin_UserManagement']")
users = driver.find_element(By.XPATH, "//*[@id='menu_admin_viewSystemUsers']")


actions = ActionChains(driver)
actions.move_to_element(admin).click().perform()
time.sleep(2)
actions.move_to_element(usermgnt).click().perform()
time.sleep(2)
actions.move_to_element(users).click().perform()
