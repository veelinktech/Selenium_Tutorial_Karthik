import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.rediff.com")
driver.maximize_window()
driver.implicitly_wait(30)
we1 = driver.find_element(By.XPATH, "//a[@title='Lightning fast free email']").text
print(we1)
time.sleep(5)
# driver.switch_to.frame("moneyiframe") # using id
# driver.switch_to.frame("moneyiframe")  # using name
# driver.switch_to.frame(0)  # using index
ele = driver.find_element(By.XPATH,"//iframe[@title='Rediff Money Widget']")

driver.switch_to.frame(ele)

f1 = driver.find_element(By.XPATH, "//span[text()='BSE']").text
print(f1)

driver.switch_to.default_content()

webpage_text = driver.find_element(By.LINK_TEXT,"Money").text
print(webpage_text)
