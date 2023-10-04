from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Locators


class TestMoveToConstructor:
    def test_move_to_constructor_by_click_on_button(self, login):
        driver = login
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.EXIT_BUTTON))
        driver.find_element(*Locators.CONSTRUCTOR).click()
        order_button = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON)).text

        assert order_button == 'Оформить заказ'
        driver.quit()

    def test_move_to_constructor_by_click_on_logo(self, login):
        driver = login
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.EXIT_BUTTON))
        driver.find_element(By.CLASS_NAME, "AppHeader_header__logo__2D0X2").click()
        order_button = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON)).text

        assert order_button == 'Оформить заказ'
        driver.quit()

