import os

from selenium.common.exceptions import NoSuchElementException

import XLUtils
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)

driver.get("http://www.lefthand.pl/pl/")

path= os.getcwd() + '\exel1.xlsx'

row = XLUtils.getRowCount(path,"Sheet1")

for r in range(2,row+1):
    username = XLUtils.readData(path,"Sheet1",r,1)
    password = XLUtils.readData(path,"Sheet1",r,2)

    driver.find_element_by_name("email").send_keys(username)
    driver.find_element_by_name("pass").send_keys(password)

    driver.find_element_by_xpath("//input[@value='submit']").click()


    try:
        logout = driver.find_element_by_xpath("//a[text()='licencjonowanie']")
        logout1 = True
    except NoSuchElementException:
        logout1 = False

    #print(driver.title)
    if logout1 == True:
        print("test is passed")
        print(driver.title)
        XLUtils.writeData(path,"Sheet1",r,3,"test passed")
        driver.find_element_by_xpath("//img[@alt='wyloguj']").click()

    else:
        print("test failed")
        XLUtils.writeData(path, "Sheet1", r, 3, "test failed")