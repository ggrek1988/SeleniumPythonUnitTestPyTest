from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)

driver.get("http://www.lefthand.pl")
userElement = driver.find_element_by_name("email")

print(userElement.is_displayed())  # return true/false based od element status
print(userElement.is_enabled())  # return true/false
userElement.send_keys("email")

passwordElement = driver.find_element_by_name("pass")

print(passwordElement.is_displayed())  # return true/false based od element status
print(passwordElement.is_enabled())  # return true/false
passwordElement.send_keys("haslo")

# driver.is_selected only use for radiobuton

driver.find_element_by_xpath("//input[@value='submit']").click()

driver.find_element_by_xpath("//*[ text() =' Witaj mmmggg.']")

driver.close()
