import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from tests.locators import Locators
from tests.constants import Constants


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(options=options, service=service)

    yield browser
    browser.quit()


@pytest.fixture()
def login(driver):
    driver.get('https://stellarburgers.nomoreparties.site/login')
    driver.find_element(*Locators.USERNAME).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.SIGN_IN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ACCOUNT_BUTTON))
    return driver
