from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opt)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
# normalize space xpath
driver.find_element(By.XPATH, "//button[normalize-space(text()='Login')]").click()
