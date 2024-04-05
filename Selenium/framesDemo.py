from selenium import webdriver
from selenium.webdriver.common.by import By

# launch browser
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

# launch url
driver.get("https://the-internet.herokuapp.com/iframe")

# switch back to frame using frame-id or name tag
driver.switch_to.frame("mce_0_ifr")

# handling elements inside frame
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate frames")

# switch back to browser from frame
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)

"""
NOTE: Without switching frame, if you try to handle elements inside frame it will throw no such element exception
Make sure to switch_to right content as per test step in any given scenario
"""