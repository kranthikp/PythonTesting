import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# handling wait
driver = webdriver.Chrome()
driver.implicitly_wait(5)
# handling explicit waits
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

# Assignment collect items name and push to list and assert
results = driver.find_elements(By.XPATH, "//div[@class='products']/div") # list[]
count = len(results)
assert count > 0
expected_items = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actual_items = []


# chaining of web elements to construct dynamically
# this loop iterates 3 times and click add button
for result in results:
    actual_items.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()

assert expected_items == actual_items

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "td:nth-child(5) p")
Sum = 0
for price in prices:
    Sum = Sum + int(price.text)

print(Sum)
totalAmount = driver.find_element(By.CSS_SELECTOR, ".totAmt").text
print(totalAmount)

assert Sum == int(totalAmount)

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

discountedAmount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert float(totalAmount) > discountedAmount





