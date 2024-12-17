from selenium import webdriver


def test_Google():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    actual_title = driver.title
    assert actual_title == "Google"
    driver.close()


def test_fb():
    driver = webdriver.Chrome()
    driver.get("https://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    actual_title = driver.title
    assert actual_title == "Facebook – log in or sign up"
    driver.close()


def test_insta():
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    actual_title = driver.title
    assert actual_title == "Instagram"


def test_rediff():
    driver = webdriver.Chrome()
    driver.get("https://www.rediff.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    actual_title = driver.title
    assert actual_title == "Rediff.com: News | Rediffmail | Stock Quotes | Shopping"
    driver.close()


def test_twitter():
    driver = webdriver.Chrome()
    driver.get("https://x.com/")
    driver.maximize_window()
    driver.implicitly_wait(30)
    actual_title = driver.title
    assert actual_title == "X. It’s what’s happening / X"
    driver.close()
