import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("all_browser")
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
