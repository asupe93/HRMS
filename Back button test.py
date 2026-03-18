from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://orangehrm.com/")

driver.maximize_window()
time.sleep(5)

# Back to Projects button (correct locator)
back_btn = driver.find_element(By.XPATH, "//a[contains(@href,'projects')]")

# Scroll + JS click (fix for click issue)
driver.execute_script("arguments[0].scrollIntoView();", back_btn)
time.sleep(1)
driver.execute_script("arguments[0].click();", back_btn)

time.sleep(5)

print("Current URL:", driver.current_url)

# verify correct page
assert "projects" in driver.current_url

print("PASS ✅ Back to Projects working")

time.sleep(10)
driver.quit()
