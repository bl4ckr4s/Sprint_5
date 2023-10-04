import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Locators


class TestRegistration:
    def test_registration_with_valid_password(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(By.XPATH, "//form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys(f'test{random.randint(100, 999)}')
        driver.find_element(By.XPATH, "//form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys(f'test{random.randint(100, 999)}@ya.ru')
        driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys('123456')
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Войти')]")))
        form_title = driver.find_element(By.XPATH, "//h2[contains(text(),'Вход')]").text

        assert form_title == 'Вход'
        driver.quit()

    def test_registration_with_invalid_password(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(By.XPATH, "//form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys('test')
        driver.find_element(By.XPATH, "//form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys('test_qa_python_1_1123@ya.ru')
        driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys('12345')
        driver.find_element(*Locators.REG_BUTTON).click()

        error_message = driver.find_element(By.XPATH, "//p[@class = 'input__error text_type_main-default']").text
        assert error_message == 'Некорректный пароль'
        driver.quit()

