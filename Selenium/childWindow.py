from selenium import webdriver
from selenium.webdriver.common.by import By

# launch browser
driver = webdriver.Firefox()
driver.implicitly_wait(2)

# launch url
driver.get("https://the-internet.herokuapp.com/windows")

# click link "Click Here"
driver.find_element(By.LINK_TEXT, "Click Here").click()

# getting list of open windows/tabs
open_windows = driver.window_handles

# switching to child window and assert header tag
driver.switch_to.window(open_windows[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
assert "New Window" == driver.find_element(By.TAG_NAME, "h3").text
driver.close()

# switching back to parent window and assert header tag
driver.switch_to.window(open_windows[0])
print(driver.find_element(By.TAG_NAME, "h3").text)
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text
driver.close()
