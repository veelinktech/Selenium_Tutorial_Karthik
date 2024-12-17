import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import XLUtils

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(30)
path = "C:\\Users\\pc\\Desktop\\DDF_V1.xlsx"

rows = XLUtils.getRowCount(path,"Sheet7")

for r in range(2,rows+1):
    un = XLUtils.readData(path,"Sheet7",r,1)
    pwd = XLUtils.readData(path,"Sheet7",r,2)

    driver.find_element(By.NAME,"username").send_keys(un)
    driver.find_element(By.NAME,"password").send_keys(pwd)
    driver.find_element(By.XPATH,"//button[normalize-space(text()='Login')]").click()
    time.sleep(5)

    homepage_text = driver.find_element(By.XPATH,"//h6[text()='Dashboard']").text

    if homepage_text =="Dashboard":
        XLUtils.writeData(path,"Sheet7",r,3,"Pass")
        driver.find_element(By.CLASS_NAME,"oxd-userdropdown-name").click()
        time.sleep(3)
        driver.find_element(By.LINK_TEXT,"Logout").click()
        time.sleep(3)

else:
    XLUtils.writeData(path,"Sheet7",r,3,"Fail")
    driver.close()