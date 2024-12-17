import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//a[text()='Create new account']").click()
parent_window = driver.current_window_handle
driver.find_element(By.ID,"terms-link").click()
child_window = driver.window_handles

for child in child_window:

    if parent_window != child:
        driver.switch_to.window(child)
        driver.find_element(By.ID,"email").send_keys("karthik")
        driver.find_element(By.ID,"pass").send_keys("karthik@123")
        child_window_text = driver.find_element(By.XPATH,"//h2[text()='Terms of Service']").text
        print(child_window_text)
        time.sleep(5)
        #driver.close()
driver.switch_to.window(parent_window)
driver.find_element(By.NAME,"firstname").send_keys('Siva')
time.sleep(5)
driver.quit()

