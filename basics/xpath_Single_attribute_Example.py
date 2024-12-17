import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.fb.com")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@placeholder='Email address or phone number']").send_keys("Karthik")
driver.find_element(By.XPATH,"//input[@data-testid='royal_pass']").send_keys("Karthik@123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(10)