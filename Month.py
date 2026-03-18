from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# browser open
driver = webdriver.Chrome()
driver.get("https://dvpro.co.in/calendar")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

print("Test Started 🚀")

# current month get karo
month = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'March')]"))
)

print("Before:", month.text)

# Next button click
next_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Next')]"))
)
next_btn.click()

# new month verify (April)
new_month = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'April')]"))
)

print("After:", new_month.text)

# assertion
assert "April" in new_month.text

print("PASS ✅ Month changed successfully")

# 👇 yaha hold karega 10 sec
time.sleep(10)

driver.quit()