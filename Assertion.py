from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://orangehrm.com/")

driver.maximize_window()
time.sleep(3)

# Next button click
month = driver.find_element(By.XPATH, "//div[contains(text(),'March')]")
print(month.text)

time.sleep(10)
