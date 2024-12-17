# Waiting statements --> implicitly wait, explicitly-wait, fluent wait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# what is Explicitly wait?
# driver can wait for a particular time to load particular web elements into the web page

opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.fb.com")
driver.maximize_window()
driver.find_element(By.PARTIAL_LINK_TEXT,"new a").click()

wait = WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.NAME,'firstname'))).send_keys('Karthik')

#driver.find_element(By.NAME,"firstname").send_keys("Karthik")
driver.find_element(By.NAME,"lastname").send_keys("O")
driver.find_element(By.NAME,"reg_email__").send_keys('9434984330')
driver.find_element(By.ID,"password_step_input").send_keys('Karthik@123')
