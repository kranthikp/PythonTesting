"""
automation requirement
1. launch url "https://rahulshettyacademy.com/loginpagePractise/"
2. click on link on top left "Free Access to ..."
3. navigate to child window
4. collect email id "mentor@rahulshettyacademy.com from the text on page use parse - string, list etc
5. close child window
6. enter email in username on login page
7. enter some password
8. assert invalid error message on output
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# launch browser
driver = webdriver.Chrome()
driver.implicitly_wait(2)
# 1. launch url "https://rahulshettyacademy.com/loginpagePractise/"
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

# 2. click on link on top left "Free Access to ..."
driver.find_element(By.CLASS_NAME, "blinkingText").click()

# 3. navigate to child window
open_windows = driver.window_handles
driver.switch_to.window(open_windows[1])
para = driver.find_element(By.CSS_SELECTOR, "p[class='im-para red']").text
lists = para.split(" ")
username = ''
# 4. collect email id "mentor@rahulshettyacademy.com from the text on page use parse - string, list etc
for string in lists:
    print(string)
    if '@' in string:
        username = string
        break
print(username)
# 5. close child window
driver.close()
driver.switch_to.window(open_windows[0])

# 6. enter email in username on login page
driver.find_element(By.ID, "username").send_keys(username)

# 7. enter some password and SignIn
driver.find_element(By.ID, "password").send_keys("password")
driver.find_element(By.ID, "signInBtn").click()

# 8. print invalid error message on output
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)
driver.close()