import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.rediff.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.LINK_TEXT,"Sign in").click()
time.sleep(5)
driver.find_element(By.CLASS_NAME,"signinbtn").click()
alt = driver.switch_to.alert
time.sleep(3)
t1 = alt.text
print(t1)
time.sleep(3)
alt.accept()


# by default driver is focused on webpage
# driver focus switch to alert popup --> driver.switch_to.alert
# In alert popup we want click ok button --> accept method
# In case alert popup we want click on cancel button --> dismiss method
# In case we want type the text in alert popup --> sendkeys
# In case we want to take the text in alert popup --> text

