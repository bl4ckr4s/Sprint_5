import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from tests.locators import Locators


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
    driver.find_element(By.XPATH, ".//input[@name='name']").send_keys('topuzliev_qa_python@ya.ru')
    driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys('123456')
    driver.find_element(*Locators.SIGN_IN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ACCOUNT_BUTTON))
    return driver

