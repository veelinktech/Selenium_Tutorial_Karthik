import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope='class')
def init_Chrome(request):
    ch_driver = webdriver.Chrome()
    request.cls.driver = ch_driver
    yield
    ch_driver.close()


@pytest.fixture(scope='class')
def init_Firefox(request):
    ff_driver = webdriver.Firefox()
    request.cls.driver = ff_driver
    yield
    ff_driver.close()


@pytest.fixture(scope='class')
def init_Edge(request):
    ed_driver = webdriver.Edge()
    request.cls.driver = ed_driver
    yield
    ed_driver.close()


@pytest.mark.usefixtures("init_Edge")
class Test_Base:
    pass


class Test_init_browser(Test_Base):

    def test_verifyTitle(self):
        self.driver.get("https://www.fb.com")
        actual_title = self.driver.title
        assert actual_title == "Facebook – log in or sign up"

    def test_verifyUrl(self):
        actual_url = self.driver.current_url
        assert actual_url == "https://www.facebook.com/"

    def test_veiryfblogodisplay(self):
        flag1 = self.driver.find_element(By.XPATH, "//div[@class='_8ice']/img").is_displayed()
        assert flag1 is True

    def test_verifyHomepagetext(self):
        actual_homepage_text = self.driver.find_element(By.CSS_SELECTOR, "._8eso").text
        assert actual_homepage_text == "Facebook helps you connect and share with the people in your life."

    def test_verifyLoginbtntext(self):
        actual_login_text = self.driver.find_element(By.CSS_SELECTOR, "button[name='login']").text
        assert actual_login_text == "Log in"

    def test_Forgotten_password_text(self):
        actual_forgotten_password_text = self.driver.find_element(By.PARTIAL_LINK_TEXT, "word?").text
        assert actual_forgotten_password_text == "Forgotten password?"

    def test_Create_new_account(self):
        actual_cna_text = self.driver.find_element(By.LINK_TEXT, "Create new account").text
        assert actual_cna_text == "Create new account"
