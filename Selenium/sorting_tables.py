"""
Miscellaneous: Handling Javascript Executor, Handling Web Tables, Chrome Options --headless --head mode
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# launch browser
driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.maximize_window()

# launch url
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# click column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

browser_sorted_veggies = []
# collect all veggies names -> browser_sorted_veggie_list
veggie_web_elements = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggie_web_elements:
    browser_sorted_veggies.append(ele.text)

actual_browser_sorted_list = browser_sorted_veggies.copy()

# sort the veggie_list => new_sorted_veggie_list
browser_sorted_veggies.sort()

# assert browser_sorted_veggie_list == new_sorted_veggie_list
assert browser_sorted_veggies == actual_browser_sorted_list
