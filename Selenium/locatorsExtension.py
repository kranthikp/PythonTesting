import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome
driver = webdriver.Chrome()
time.sleep(2)
# launch the url
driver.get("https://rahulshettyacademy.com/client")
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
time.sleep(2)
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@12345")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@12345")
time.sleep(2)
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
time.sleep(2)
