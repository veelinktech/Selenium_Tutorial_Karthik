# select --> class, method--> selectbyvisibletext, selectbyvalue, selectbyindex
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Options()
s.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=s)
driver.get("https://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//a[starts-with(@id, 'u_0_0')]").click()
month_dd = driver.find_element(By.ID,"month")
time.sleep(5)
sel = Select(month_dd)
sel.select_by_visible_text("Dec")
time.sleep(5)
sel.select_by_value("2")
time.sleep(5)
sel.select_by_index(4)


'''
How to you select the drop down?
We identify the dropdown web element 
Stored in one variable
We create an object for Select class
We can pass the variable as a parameter in select class
We use the 3 method selectbyvisibletext, selectbyindex, selectbyvalue
'''
