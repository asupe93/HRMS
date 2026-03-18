from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://dvpro.co.in/")

driver.maximize_window()
wait = WebDriverWait(driver, 10)

print("Test Started 🚀")

# email
email = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))
)
email.send_keys("tester@dustvalue.com")

# password
password = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@type='password']"))
)
password.send_keys("Dustvalue@123")

# 🔥 ENTER press (form submit)
password.send_keys(Keys.ENTER)

print("Login submitted ✅")

# wait for any page change (safe)
wait.until(lambda d: d.current_url != "https://dvpro.co.in/")

print("Login done ✅")
print("Current URL:", driver.current_url)

driver.quit()