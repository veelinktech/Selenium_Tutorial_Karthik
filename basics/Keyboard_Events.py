from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("https://demo.guru99.com/test/newtours/register.php")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.NAME,"firstName").send_keys("RAM")

act = ActionChains(driver)
(((((act.send_keys(Keys.TAB).send_keys('K').
 send_keys(Keys.TAB).send_keys('9344864234').
 send_keys(Keys.TAB).send_keys("Ram@gmail.com")).
 send_keys(Keys.TAB)).send_keys("10, Anna Nagar").
 send_keys(Keys.TAB)).send_keys("Chennai").
 send_keys(Keys.TAB)).send_keys('TN').
 send_keys(Keys.TAB)).send_keys('600001').perform()