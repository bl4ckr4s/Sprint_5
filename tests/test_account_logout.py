from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Locators


class TestAccountLogout:
    def test_account_logout_in_profile(self, login):
        driver = login
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.EXIT_BUTTON))
        driver.find_element(*Locators.EXIT_BUTTON).click()
        form_title = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_FORM_TITLE)).text

        assert form_title == 'Вход'
