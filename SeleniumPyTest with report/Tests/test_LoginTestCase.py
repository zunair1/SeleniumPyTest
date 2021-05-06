from pages.LoginPage import LoginPageClass
from config.config import TestData
from Tests.test_base import basetest

class Test_doLoginTest(basetest):

    def test_do_login(self):
        driver = self.driver

        loginPageObj = LoginPageClass(driver)
        loginPageObj.setUserEmail(TestData.USER_EMAIL)
        loginPageObj.setPassword(TestData.PASSWORD)
        loginPageObj.clickLogin()

