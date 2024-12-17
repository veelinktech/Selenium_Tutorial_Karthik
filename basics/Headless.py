import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option('detach',True)
opt.add_argument("--headless")
driver = webdriver.Chrome(options=opt)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
time.sleep(3)
driver.find_element(By.XPATH,"//button[normalize-space(text()='Login')]").click()
time.sleep(3)
homepage_title = driver.title
print(homepage_title)
homepage_url = driver.current_url
print(homepage_url)
driver.find_element(By.XPATH,"//p[@class='oxd-userdropdown-name']").click()
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Logout").click()
time.sleep(3)
driver.close()