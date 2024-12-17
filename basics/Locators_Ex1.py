import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.fb.com")
driver.maximize_window()
time.sleep(5)
# using id
driver.find_element(By.ID, "email").send_keys("Karthik@gmail.com")
time.sleep(3)

# using name
driver.find_element(By.NAME, "pass").send_keys("Karthik@123")
time.sleep(10)

# using class name
f1 = driver.find_element(By.CLASS_NAME,"_8eso").text
print(f1)

# using link text
f2 = driver.find_element(By.LINK_TEXT,"Forgotten password?").text
print(f2)

# using partial link text
f3 = driver.find_element(By.PARTIAL_LINK_TEXT,"got").text
print(f3)