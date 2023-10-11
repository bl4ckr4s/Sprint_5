import random
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Locators
from tests.constants import Constants


class TestRegistration:
    def test_registration_with_valid_password(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*Locators.NAME_INPUT).send_keys(f'test{random.randint(100, 999)}')
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(f'test{random.randint(100, 999)}@ya.ru')
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys('123456')
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.SIGN_IN_BUTTON))
        form_title = driver.find_element(*Locators.LOGIN_FORM_TITLE).text

        assert form_title == 'Вход'

    def test_registration_with_invalid_password(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*Locators.NAME_INPUT).send_keys('test')
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys('12345')
        driver.find_element(*Locators.REG_BUTTON).click()

        error_message = driver.find_element(*Locators.ERROR_MESSAGE).text
        assert error_message == 'Некорректный пароль'
