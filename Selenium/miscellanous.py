"""
Miscellaneous: Handling Javascript Executor, Handling Web Tables, Chrome Options --headless --head mode
"""
import time
from selenium import webdriver
"""
using Chrome Options to run --headless
handling ssl issue using chrome options
"""
# using Chrome Options to run --headless
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

# launch browser
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(2)
driver.maximize_window()

# launch url
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Using Javascript Executor for Handling scroll and js actions
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

# taking screenshot
driver.get_screenshot_as_file("screen.png")