import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.fb.com")
driver.maximize_window()
driver.find_element(By.XPATH,"html/body/div/div/div/div/div/div/div[2]/div/div/form/div/div/input").send_keys("Ramkumar")
driver.find_element(By.XPATH,"html/body/div/div/div/div/div/div/div[2]/div/div/form/div/div[2]/div/input").send_keys("ram@123")
driver.find_element(By.XPATH,"html/body/div/div/div/div/div/div/div[2]/div/div/form/div[2]/button").click()
time.sleep(5)
f1 = driver.find_element(By.XPATH,"//div[@id='loginform']/div[2]/div[2]").text
print(f1)