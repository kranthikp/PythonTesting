import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome
driver = webdriver.Chrome()

# launch the url
driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(2)

# maximize
driver.maximize_window()

# id, xpath, cssSelector, className, name, partialLinkText, linkText
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
time.sleep(2)
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
time.sleep(2)
driver.find_element(By.ID, "exampleCheck1").click()

# XPATH - //tagname[@attribute = 'value'] -> //input[@type='submit'
# CSS - tagname[attribute = 'value'] -> input[@type='submit' #id .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Panda")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
# assertion
assert "Success" in message
time.sleep(2)

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("hello_again")
time.sleep(2)
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()