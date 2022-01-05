from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?org/openqa/selenium/cli/package-summary.html")

driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("WebDrive").click()

driver.switch_to.default_content()

time.sleep(3)
driver.switch_to.frame("classFrame")
driver.find_element_by_xpath("/html/body/header/nav/div[1]/div[1]/ul/li[6]").click()






