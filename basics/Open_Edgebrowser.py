import time

from selenium import webdriver

driver = webdriver.Edge()
driver.get("http://www.instagram.com")
time.sleep(5)
driver.minimize_window()
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.close()