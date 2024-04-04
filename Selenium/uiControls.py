from selenium import webdriver
from selenium.webdriver.common.by import By

# handling auto-suggestive dynamic dropdown
driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# handling checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

# handling radio buttons
radio_buttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radio_buttons[2].click()
assert radio_buttons[2].is_selected()

# assert is_displayed
assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed() # negation assertion




