import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# handling auto-suggestive dynamic dropdown
driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

# print(driver.find_element(By.ID, "autosuggest").text)
display_text = driver.find_element(By.ID, "autosuggest").get_attribute("value")
assert display_text == "India"
