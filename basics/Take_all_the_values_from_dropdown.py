from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.LINK_TEXT,"Create new account").click()
year_dd = driver.find_element(By.XPATH,"//select[@title='Year']")
sel = Select(year_dd)
year_list = sel.options
print(len(year_list))

for i in year_list:
    print(i.text)