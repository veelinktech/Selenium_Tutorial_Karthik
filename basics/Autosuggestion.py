from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.google.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.NAME, "q").send_keys("javascript")
li = driver.find_elements(By.XPATH, "//div[@class='erkvQe']/div/ul/li")
print(len(li))

# for i in li:
#     print(i.text)

for i in li:
    if i.text == "javascript data types":
        i.click()
        break
