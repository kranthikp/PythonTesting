import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# launch browser
driver = webdriver.Chrome()

# implicit wait
driver.implicitly_wait(5)

url = "https://rahulshettyacademy.com/seleniumPractise/#/"
# launch url - Green Kart Website
driver.get(url)

# find search bar and enter "ber"
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

# Assignment collect items name and push to list and assert
# collect result items to add to cart in a list
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

# validate cart items
assert expected_items == actual_items

# click on Cart
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

# click PROCEED TO CHECKOUT
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "td:nth-child(5) p")
Sum = 0
for price in prices:
    print(price.text)
    Sum = Sum + int(price.text)

# print Sum & totalAmount
print("Sum {}".format(Sum))
totalAmount = driver.find_element(By.CSS_SELECTOR, ".totAmt").text
print("totalAmount "+totalAmount)

# validate total sum & amount
assert Sum == int(totalAmount)

# enter promocode
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")

# click apply
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# explicit wait on specific case
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
discountedAmount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

# validate totalAmount > discountedAmount
assert float(totalAmount) > discountedAmount

# click place order
driver.find_element(By.XPATH, "//button[text()='Place Order']").click()

# assert Choose Country Label on page
driver.find_element(By.XPATH, "//label[text()='Choose Country']").is_displayed()

# select India from dropdown
country_dropdown = Select(driver.find_element(By.TAG_NAME, "select"))
country_dropdown.select_by_value("India")
time.sleep(2)

# check Agree Checkbox
driver.find_element(By.CLASS_NAME, "chkAgree").click()

# click Proceed
driver.find_element(By.XPATH, "//button[text()='Proceed']").click()

# validate "brand greenLogo" is displayed
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='brand greenLogo']")))
driver.find_element(By.CSS_SELECTOR, "div[class='brand greenLogo']").is_displayed()

# validate navigated back to home
current_url = driver.current_url
assert url in current_url
print(current_url)

