import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.fb.com")
driver.maximize_window()
time.sleep(5)
driver.get("https://www.google.com")
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()
time.sleep(5)
driver.close()