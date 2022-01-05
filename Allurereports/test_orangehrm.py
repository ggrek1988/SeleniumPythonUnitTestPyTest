from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.firefox.service import Service




@allure.severity(allure.severity_level.NORMAL)
class TestHRM:

    @allure.severity(allure.severity_level.MINOR)
    def test_Logo(self):
        self.ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
        self.op = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(service=self.ser, options=self.op)

        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        status = self.driver.find_element_by_xpath("//*[@id='divLogo']/img").is_displayed()

        if status == True:
            assert True
        else:
            assert False

        self.driver.close()

    #@allure.severity(allure.severity_level.BLOCKER)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_listemployees(self):
        pytest.skip("Skipping test... Later i will implement")

    @allure.severity(allure.severity_level.NORMAL)
    def test_Login(self):
        self.ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
        self.op = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(service=self.ser, options=self.op)

        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        act_title = self.driver.title

        if act_title == "OrangeHRM123":
            self.driver.close()
            assert  True
        else:
            allure.attach(self.driver.get_full_page_screenshot_as_png(),name="testLoginScreen",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False


