import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//a[@data-testid='open-registration-form-button']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@class='_8esa'][@value='2']").click()
time.sleep(10)