import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# launch browser
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# action class for mouse actions
action = ActionChains(driver)

# move to element to mouse hover button
action.move_to_element(driver.find_element(By.XPATH, "//button[@id='mousehover']")).perform()
# action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

# other mouse actions
# action.drag_and_drop()
# action.double_click()
# action.context_click()

