from selenium import webdriver
from selenium.webdriver.common.by import By

# handling auto-suggestive dynamic dropdown
driver = webdriver.Chrome()

# handling alerts
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name = "panda"
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()

# switch driver browser to alert mode/frame/window
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
assert name in alert_text
alert.accept() # to click on ok button
# alert.dismiss() # to click on cancel button

