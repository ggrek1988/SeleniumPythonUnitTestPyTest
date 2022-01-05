from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)

WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH,
                                                                    "//label[@for='RESULT_RadioButton-7_0']")))
driver.find_element(By.ID, "RESULT_RadioButton-7_0").click()

status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)
