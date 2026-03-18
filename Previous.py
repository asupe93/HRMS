from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://dvpro.co.in/calendar")

driver.maximize_window()
time.sleep(3)

# Next button click
prev_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Previous')]")
prev_btn.click()

time.sleep(10)