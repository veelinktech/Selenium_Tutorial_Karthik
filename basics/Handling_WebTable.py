from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa?src=gain_lose")
driver.maximize_window()
driver.implicitly_wait(30)
# Single column
ele1 = driver.find_element(By.XPATH,"//table[@class='dataTable']//tr[5]/td[1]").text
print(ele1)
# Entire row
ele2 = driver.find_element(By.XPATH,"//table[@class='dataTable']//tr[5]").text
print(ele2)

# Entire table
entireTable = driver.find_elements(By.XPATH,"//table[@class='dataTable']//tr")
print(len(entireTable))

for i in entireTable:
    print(i.text)