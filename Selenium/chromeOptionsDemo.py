"""
Miscellaneous: Handling Javascript Executor, Handling Web Tables, Chrome Options --headless --head mode
"""
from selenium import webdriver

# chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
# chrome_options.add_argument("--disable-gpu")

# launch browser
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(2)

# launch url
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title) # ProtoCommerce

