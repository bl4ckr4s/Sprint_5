from selenium.webdriver.common.by import By


class Locators:
    REG_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]") # Кнопка «Зарегистрироваться»
    SIGN_IN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]") # Кнопка «Войти»
    ACCOUNT_BUTTON = (By.XPATH, ".//a[@href = '/account']") # Ссылка на «Личный Кабинет»
    CONSTRUCTOR = (By.XPATH, "//p[contains(text(), 'Конструктор')]") # Ссылка на «Конструктор»
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]") # Кнопка «Оформить заказ»
    EXIT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]") # Кнопка «Выход»
    USERNAME = (By.XPATH, ".//input[@name='name']") # Имя пользователя
    PASSWORD = (By.XPATH, ".//input[@name='Пароль']") # Пароль
    ACTIVE_SECTION = (By.CSS_SELECTOR, ".tab_tab_type_current__2BEPc>span") # Активный раздел в блоке «Соберите бургер»





