import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Chrome driver service - selenium checks Chrome version and download & loads 160->160 chrome driver
# used only if # VPN issue observed in Client blocking Chrome version check

# service_obj = Service("../Selenium/chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)

# Invoking Browser and Running Tests in Chrome, Edge, Firefox
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Edge()

driver.get("https://rahulshettyacademy.com")
time.sleep(2)
driver.maximize_window()

print(driver.title)
print(driver.current_url)
