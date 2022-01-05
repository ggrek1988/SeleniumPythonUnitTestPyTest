from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)
driver.get("http://www.lefthand.pl")

driver.implicitly_wait(10)  # jesli nie znajdzie elementu kazdego uzytego, w tescie wtedy bedzie odpytywał 10 sekund
driver.find_element_by_xpath("//input[@value='submit']").click()

print(driver.title)
assert "Program księgowy LeftHand - program do księgowości dla firm" in driver.title
