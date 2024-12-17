from selenium import webdriver
from selenium.webdriver.common.by import By


def test_Fb():
    driver = webdriver.Chrome()
    driver.get("https://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)

    actual_title = driver.title
    print("Testcase1 Start")
    assert actual_title == "Facebook – log in or sign u"
    print("Testcase1 Completed")

    actual_url = driver.current_url
    print("Testcase2 Start")
    assert actual_url == "https://www.facebook.com/"
    print("Testcase2 Completed")

    print("Testcase3 Start")
    flag1 = driver.find_element(By.XPATH,"//div[@class='_8ice']/img").is_displayed()
    assert flag1 is True
    print("Testcase3 Completed")