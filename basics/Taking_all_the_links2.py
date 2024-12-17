from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.rediff.com/")
driver.maximize_window()
driver.implicitly_wait(30)
a_list = driver.find_elements(By.TAG_NAME,"a")
print(len(a_list))

for i in a_list:
    print(i.get_attribute("href"))
