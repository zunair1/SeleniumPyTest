import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='class')
def init_driver(rs):
    options = Options()
    options.headless = True
    rs.driver = webdriver.Chrome(executable_path="D:/SeleniumPyTest/chromedriver_win32/chromedriver.exe",
                                  options=options)
    rs.driver.get("https://microaccounttest.ihpapp.com/")
    rs.driver.maximize_window()
    yield
    rs.driver.quit()