# Waiting statements --> implicitly wait, explicitly-wait, fluent wait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# what is implicitly wait?
# driver can wait for a particular time to load all the web elements into the web page

opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.PARTIAL_LINK_TEXT,"new a").click()
driver.find_element(By.NAME,"firstname").send_keys("Karthik")
driver.find_element(By.NAME,"lastname").send_keys("O")
driver.find_element(By.NAME,"reg_email__").send_keys('9434984330')
driver.find_element(By.ID,"password_step_input").send_keys('Karthik@123')
