class locators:
    """LOGIN PAGE LOCATORS"""

    Email_By_NAME = "email"
    Password_By_NAME = "password"
    LoginButton_By_XPATH = "//button[@type='submit']"
    LoginWelcomeText_By_XPATH = "//div[contains(text(),'logged in successfully')]"

    """LOGOUT LOCATORS"""

    UserProfileButton_By_XPATH = "//body/div[2]/div[1]/div[2]/div[1]/div[2]/button[1]/img[1]"
    LogoutButton_By_XPATH = "//li[contains(text(),'log out')]"

    """SIGN UP LOCATORS"""

    SignUpButtonOnHomePage_By_XPATH = "//div[contains(text(),'Sign Up')]"
    SignUpEmail_By_ID = "user_email"
    SignUpPassword_By_NAME = "passwordHash"
    SignUpConfirmPassword_By_NAME = "password2"
    SignUpButtonOnSignUpPage_By_CLASS_NAME = "btn-primary"
    SignUpSuccessMessage_By_XPATH = "//div[contains(text(),'You have registered successfully')]"

    """UPLOAD CSV LOCATORS"""

    VIEW_CSV_BUTTON_By_LINK_TEXT = "View csvs"
    NEW_CSVS_Add_Button_By_LINK_TEXT = "+ New"
    BROWSE_FILE_BUTTON_By_NAME = "file"
    SUBMIT_FILE_BUTTON_By_XPATH = "//button[contains(text(),'Submit')]"

    """DELETE CSV LOCATORS"""
    DELETE_CSV_BUTTON_By_XPATH = "//a[contains(text(),'Delete')]"
    DELETE_CSV_SUCCESS_MESSAGE_By_XPATH = "/html[1]/body[1]/div[1]"

    """Update setting"""

    CLICK_SETTINGS = "//li[contains(text(),'settings')]"
    INPUT_BOX = "//input[@name='userName']"
    CLICK_SAVE = "//button[@class='btn-3']"


    """filter csv data"""
    CLICK_DIALOG = "csvDates"
    SELECT_26 = "//div[@class='dayContainer'] /span[30]"
    SELECT_28 = "//div[@class='dayContainer'] /span[32]"
    CLICK_FILTER = "//button[@type='submit']"

