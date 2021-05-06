from Locators.locatorsOfWebsite import locators


class SignUpPageClass:

    def __init__(self, driver):
        self.driver = driver

        self.SignUpUrlButton = locators.SignUpButtonOnHomePage_By_XPATH
        self.SignUpEmail = locators.SignUpEmail_By_ID
        self.SignUpPassword = locators.SignUpPassword_By_NAME
        self.SignUpConfirmPassword = locators.SignUpConfirmPassword_By_NAME
        self.SignUpButtonOnSignUpPage = locators.SignUpButtonOnSignUpPage_By_CLASS_NAME
        self.SignUpSuccessMessage = locators.SignUpSuccessMessage_By_XPATH

    """SignUp actions functions"""

    def clickSignUpButtonOnHomePage(self):
        self.driver.find_element_by_xpath(self.SignUpUrlButton).click()

    def setSignUpUserEmail(self, SignUpEmail):
        self.driver.find_element_by_id(self.SignUpEmail).send_keys(SignUpEmail)

    def setSignUpPassword(self, SignUpPassword):
        self.driver.find_element_by_name(self.SignUpPassword).send_keys(SignUpPassword)

    def setSignUpConfirmPassword(self, SignUpConfirmPassword):
        self.driver.find_element_by_name(self.SignUpConfirmPassword).send_keys(SignUpConfirmPassword)

    def clickSignUp(self):
        self.driver.find_element_by_class_name(self.SignUpButtonOnSignUpPage).click()

    def SignUpSuccessMessage(self):
        textSignUp = self.driver.find_element_by_xpath(self.SignUpSuccessMessage)
        return textSignUp.text
