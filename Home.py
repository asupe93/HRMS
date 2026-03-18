from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get(https://orangehrm.com/")

driver.maximize_window()
time.sleep(5)

print("Test Started 🚀")

# find element using partial text anywhere
home_btn = driver.find_element(By.XPATH, "//*[contains(text(),'Home')]")

# scroll + JS click
driver.execute_script("arguments[0].scrollIntoView();", home_btn)
time.sleep(1)
driver.execute_script("arguments[0].click();", home_btn)

time.sleep(5)

print("Current URL:", driver.current_url)

time.sleep(10)
driver.quit()
