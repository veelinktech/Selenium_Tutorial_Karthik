import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.fb.com")
driver.maximize_window()
actual_title = driver.title
print(actual_title)
time.sleep(5)
actual_url = driver.current_url
print(actual_url)
time.sleep(5)
actual_name = driver.name
print(actual_name)
time.sleep(5)