import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def init_Chrome():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield
    driver.close()


@pytest.fixture(scope='module')
def init_Firefox():
    global driver
    driver = webdriver.Firefox()
    driver.get("https://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield
    driver.close()


@pytest.fixture(scope='module')
def init_Edge():
    global driver
    driver = webdriver.Edge()
    driver.get("https://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield
    driver.close()


@pytest.mark.usefixtures("init_Edge")
def test_verifyTitle():
    actual_title = driver.title
    assert actual_title == "Facebook – log in or sign up"


@pytest.mark.usefixtures("init_Edge")
def test_verifyUrl():
    actual_url = driver.current_url
    assert actual_url == "https://www.facebook.com/"


@pytest.mark.usefixtures("init_Edge")
def test_veiryfblogodisplay():
    flag1 = driver.find_element(By.XPATH, "//div[@class='_8ice']/img").is_displayed()
    assert flag1 is True


@pytest.mark.usefixtures("init_Edge")
def test_verifyHomepagetext():
    actual_homepage_text = driver.find_element(By.CSS_SELECTOR,"._8eso").text
    assert actual_homepage_text == "Facebook helps you connect and share with the people in your life."


@pytest.mark.usefixtures("init_Edge")
def test_verifyLoginbtntext():
    actual_login_text = driver.find_element(By.CSS_SELECTOR,"button[name='login']").text
    assert actual_login_text == "Log in"


@pytest.mark.usefixtures("init_Edge")
def test_Forgotten_password_text():
    actual_forgotten_password_text = driver.find_element(By.PARTIAL_LINK_TEXT,"word?").text
    assert actual_forgotten_password_text == "Forgotten password?"


@pytest.mark.usefixtures("init_Edge")
def test_Create_new_account():
    actual_cna_text = driver.find_element(By.LINK_TEXT,"Create new account").text
    assert actual_cna_text == "Create new account"
