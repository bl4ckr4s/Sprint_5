from tests.locators import Locators


class TestConstructor:
    def test_buns_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.SAUCES_SECTION).click()
        driver.find_element(*Locators.BUNS_SECTION).click()
        section = driver.find_element(*Locators.ACTIVE_SECTION).text
        assert section == 'Булки'

    def test_sauces_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.SAUCES_SECTION).click()
        section = driver.find_element(*Locators.ACTIVE_SECTION).text
        assert section == 'Соусы'

    def test_stuffing_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.STUFFING_SECTION).click()
        section = driver.find_element(*Locators.ACTIVE_SECTION).text
        assert section == 'Начинки'
