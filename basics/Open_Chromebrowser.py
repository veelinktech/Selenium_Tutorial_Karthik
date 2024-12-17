import time

from selenium import webdriver

driver = webdriver.Chrome() # open the empty chrome browser
driver.get("http://www.google.com")
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.minimize_window()
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.close()