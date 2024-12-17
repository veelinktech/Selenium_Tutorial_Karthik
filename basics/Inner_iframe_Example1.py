from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe")
driver.maximize_window()
driver.implicitly_wait(30)
# main frame
driver.switch_to.frame("iframeResult")

# inner frame
inner_frame = driver.find_element(By.XPATH,"//iframe[@title='W3Schools Free Online Web Tutorials']")
driver.switch_to.frame(inner_frame)

ele = driver.find_element(By.LINK_TEXT,"JAVASCRIPT").text
print(ele)