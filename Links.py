from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

links = driver.find_elements(By.TAG_NAME, "a")
print("Number of links presents:", len(links))  # Print how many links present in a page

for link in links:
    print(link.text)

# clicking on the link
driver.find_element(By.LINK_TEXT, "Software Testing Tutorials").click()
