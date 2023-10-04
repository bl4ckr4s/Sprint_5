from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Locators


class TestConstructor:
    def test_buns_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, "//span[contains(text(),'Соусы')]").click()
        driver.find_element(By.XPATH, "//span[contains(text(),'Булки')]").click()
        section = driver.find_element(*Locators.ACTIVE_SECTION).text
        assert section == 'Булки'
        driver.quit()

    def test_sauces_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, "//span[contains(text(),'Соусы')]").click()
        section = driver.find_element(*Locators.ACTIVE_SECTION).text
        assert section == 'Соусы'
        driver.quit()

    def test_stuffing_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, "//span[contains(text(),'Начинки')]").click()
        section = driver.find_element(*Locators.ACTIVE_SECTION).text
        assert section == 'Начинки'
        driver.quit()
