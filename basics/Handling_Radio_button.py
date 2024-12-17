from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opt)
driver.get("https://register.rediff.com/register/register.php?FormName=user_details")
driver.maximize_window()
female_radio = driver.find_element(By.XPATH,"//input[starts-with(@name,'gender')][@value='f']")

f1 = female_radio.is_displayed()
print("Female radio button is display = ", f1)

f2 = female_radio.is_enabled()
print("Female radio button is enable = ", f2)

f3 = female_radio.is_selected()
print("Female radio button is select = ", f3)

female_radio.click()

f4 = female_radio.is_selected()
print("After clicking female radio button is select = ", f4)