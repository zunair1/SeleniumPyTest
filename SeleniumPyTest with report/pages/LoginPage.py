from Locators.locatorsOfWebsite import locators


class LoginPageClass:

    def __init__(self, driver):
        self.driver = driver

        self.Email = locators.Email_By_NAME
        self.Password = locators.Password_By_NAME
        self.LoginButton = locators.LoginButton_By_XPATH
        self.LoginWelcomeText = locators.LoginWelcomeText_By_XPATH

        self.userProfileImage = locators.UserProfileButton_By_XPATH
        self.LogoutButton = locators.LogoutButton_By_XPATH

    """Page actions functions"""

    def setUserEmail(self, Email):
        self.driver.find_element_by_name(self.Email).send_keys(Email)

    def setPassword(self, password):
        self.driver.find_element_by_name(self.Password).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.LoginButton).click()

    def loginSuccessMessage(self):
        element = self.driver.find_element_by_xpath(self.LoginWelcomeText)
        return element.text

    def clickUserProfileButton(self):
        self.driver.find_element_by_xpath(self.userProfileImage).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.LogoutButton).click()
