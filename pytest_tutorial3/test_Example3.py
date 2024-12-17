import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("init_Chrome")
class Test_Base:
    pass

class Test_Chrome_OrangeHRM(Test_Base):

    @pytest.mark.parametrize("username,password",
    [
        ("Admin","admin123"),
        ("Admin","admin123"),
        ("Admin","admin123"),
        ("admin","admin123")
    ])
    def test_Login(self, username, password):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.NAME,"username").send_keys(username)
        self.driver.find_element(By.NAME,"password").send_keys(password)
        self.driver.find_element(By.XPATH,"//button[normalize-space(text()='Login')]").click()
        actual_title = self.driver.title
        assert actual_title == "OrangeHRM"
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,".oxd-userdropdown-name").click()
        self.driver.find_element(By.LINK_TEXT,"Logout").click()