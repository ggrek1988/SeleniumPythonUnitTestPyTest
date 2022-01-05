from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

element = driver.find_element_by_id("RESULT_RadioButton-9")
drp = Select(element)

# select by visible text
# drp.select_by_visible_text("Morning")

# select by index
# drp.select_by_index(2) # Afternoon

# select by value
drp.select_by_value("Radio-2")

# Count number of options
print(len(drp.options))

# Capture all the option print them as output

all_options = drp.options

for option in all_options:
    print(option.text)
