import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("Karthik")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"#email").clear()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"input[id='email']").send_keys("Ram")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"input[name='pass']").send_keys("Ram@123")
time.sleep(3)
ele1 = driver.find_element(By.CSS_SELECTOR,"._8eso").text
print(ele1)

#cssSelector > startsiwth(^)

ele2 = driver.find_element(By.CSS_SELECTOR,"a[data-testid^='open']").text
print(ele2)

#cssSelector > contains(*)

ele3 = driver.find_element(By.CSS_SELECTOR,"a[data-testid*='form']").text
print(ele3)