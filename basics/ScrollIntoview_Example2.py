import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.geeksforgeeks.org/selenium-scrolling-a-web-page-using-java/?ref=ml_lbp")
driver.maximize_window()
time.sleep(5)
driver.execute_script()