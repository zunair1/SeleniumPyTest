import random


class TestData:

    USER_EMAIL = "test3@test.com"
    PASSWORD = "test1234"
    BASE_URL = "https://microaccounttest.ihpapp.com/"
    LOGIN_WELCOME_MESSAGE = "Michal logged in successfully"

    SIGN_UP_PASSWORD = "test1234"
    SIGN_UP_CONFIRM_PASSWORD = "test1234"
    SIGN_UP_SUCCESS_MESSAGE = "You have registered successfully"

    random_int = random.randint(0, 10000)
    signUpEmail = f'test{random_int}@test.com'

    CSV_FILE_PATH = "D:/SeleniumPyTest/resources/testAksam.csv"

    CSV_DELETE_SUCCESS_MESSAGE = "Csv deleted"

    NAMETOUPDATE = "Aksam"
