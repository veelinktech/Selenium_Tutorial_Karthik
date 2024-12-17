from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_experimental_option('detach',True)
opt.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=opt)
driver.get("https://www.justdial.com/")
driver.maximize_window()