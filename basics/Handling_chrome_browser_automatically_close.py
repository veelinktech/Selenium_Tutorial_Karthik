from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("http://www.fb.com")
driver.maximize_window()
actual_title  = driver.title
if actual_title == "Facebook":
    print("Test cases Pass")
else:
    print("Test case Fail")

driver.close()