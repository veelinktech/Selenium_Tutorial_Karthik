import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.rediff.com/")
driver.maximize_window()
time.sleep(5)
# entire screen scroll down
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

# partially scroll down
driver.execute_script("window.scrollBy(0,3000)")

time.sleep(5)
# scroll up
driver.execute_script("window.scrollBy(0,-3000)")
