from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.fb.com")
driver.maximize_window()
tv = driver.find_element(By.ID,"email").get_attribute("data-testid")
print(tv)