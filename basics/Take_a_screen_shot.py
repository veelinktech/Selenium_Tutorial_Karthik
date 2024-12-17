import time

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.instagram.com")
driver.maximize_window()
driver.implicitly_wait(30)
time.sleep(5)
driver.get_screenshot_as_file("C:\\Users\\pc\\Desktop\\Demo\\insta2.jpeg")
driver.get_full_page_screenshot_as_file("C:\\Users\\pc\\Desktop\\Demo\\insta1.png")