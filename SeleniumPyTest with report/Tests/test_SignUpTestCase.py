import unittest

import allure
from Tests.conftest import TestRunner
from pages.SignUpPage import SignUpPageClass
from config.config import TestData


class test_doSignUpTest(TestRunner):

    def test_do_SignUp(self):
        driver = self.driver

        SignUpPageObj = SignUpPageClass(driver)
        SignUpPageObj.clickSignUpButtonOnHomePage()
        SignUpPageObj.setSignUpUserEmail(TestData.signUpEmail)
        SignUpPageObj.setSignUpPassword(TestData.SIGN_UP_PASSWORD)
        SignUpPageObj.setSignUpConfirmPassword(TestData.SIGN_UP_CONFIRM_PASSWORD)
        SignUpPageObj.clickSignUp()
