import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# launch browser
service_obj = Service("../Selenium/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# implicit wait
driver.implicitly_wait(4)

# maximize
driver.maximize_window()

# launch url
driver.get("https://rahulshettyacademy.com/angularpractice/")

# click Shop on Header  .CSS=> a[href*='shop'] .XPATH =>//a[contains(@href,'shop')]
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

# get the list of items and iterate to get Blackberry then click add to cart
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for product in products:
    product_name = product.find_element(By.XPATH, "div/h4/a").text
    if product_name == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

# click checkout and complete actions
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("Ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success! Thank you!" in message
driver.close()
