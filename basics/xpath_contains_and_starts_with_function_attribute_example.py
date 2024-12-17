import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.fb.com")
driver.maximize_window()
# f1 = driver.find_element(By.XPATH,"//a[@id='u_0_0_u6']").text
# print(f1)

f2 = driver.find_element(By.XPATH,"//a[contains(@id,'_0_')]").text
print(f2)

f3 = driver.find_element(By.XPATH,"//a[starts-with(@id,'u_0_')]").text
print(f3)