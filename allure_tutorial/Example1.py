import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_OrangeHRM:

    @allure.severity(allure.severity_level.NORMAL)
    def test_verifyTitle(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        actualTitle = self.driver.title

        if actualTitle == "OrangeHRM":
            assert True
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="OrangeHRMTitle",
                          attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_verifyUrl(self):
        pytest.skip("Skip the Testcases")

    @allure.severity(allure.severity_level.NORMAL)
    def test_verifyLoginText(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        actual_text = self.driver.find_element(By.XPATH,"//h5[text()='Login']").text
        if actual_text == "Login":
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="OrangeHRMLoginTitle",
                          attachment_type=AttachmentType.PNG)
            assert False
