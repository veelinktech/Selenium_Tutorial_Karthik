import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.fb.com")
driver.maximize_window()
t1 = driver.find_element(By.XPATH,"//h2[text()='Facebook helps you connect and share with the people in your life.']").text
print(t1)

t2 = driver.find_element(By.XPATH,"//button[text()='Log in']").text
print(t2)

t3 = driver.find_element(By.XPATH,"//a[text()='Forgotten password?']").text
print(t3)
time.sleep(5)