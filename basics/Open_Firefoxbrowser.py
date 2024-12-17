import time

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.fb.com")
time.sleep(5)
driver.minimize_window()
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.close()