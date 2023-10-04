from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Locators


class TestMoveToMyAccount:
    def test_move_to_account_by_click_on_account_button(self, login):
        driver = login
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        exit_button = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Выход')]"))).text

        assert exit_button == 'Выход'
        driver.quit()




