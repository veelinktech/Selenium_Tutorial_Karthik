import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.fb.com")
driver.maximize_window()
f1 = driver.find_element(By.XPATH,"//h2[text()='Facebook helps you connect and share with the people in your life.']").text
print(f1)

f2 = driver.find_element(By.XPATH,"//h2[contains(text(),'your life')]").text
print(f2)

f3 = driver.find_element(By.XPATH,"//h2[starts-with(text(),'F')]").text
print(f3)


# using text function
t1 = driver.find_element(By.XPATH,"//a[text()='Forgotten password?']").text
print(t1)

# using contains function

t2 = driver.find_element(By.XPATH,"//a[contains(text(),'got')]").text
print(t2)

# using starts-with function
t3 = driver.find_element(By.XPATH,"//a[starts-with(text(),'Fo')]").text
print(t3)

time.sleep(5)
