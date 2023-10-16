from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Locators
from tests.constants import Constants


class TestAuthorisation:

    def test_authorization_on_the_homepage(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.USERNAME).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()

        order_button = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON)).text
        assert order_button == 'Оформить заказ'

    def test_authorization_on_my_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.USERNAME).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()

        order_button = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON)).text
        assert order_button == 'Оформить заказ'

    def test_authorization_on_registration_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.USERNAME).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()

        order_button = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON)).text
        assert order_button == 'Оформить заказ'
