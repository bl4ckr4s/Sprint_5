from selenium.webdriver.common.by import By


class Locators:
    NAME_INPUT = (By.XPATH, "(//input[@name='name'])[1]") # Поле «Имя»
    EMAIL_INPUT = (By.XPATH, "(//input[@name='name'])[2]") # Поле «Email»
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']") # Поле «Пароль»
    ERROR_MESSAGE = (By.XPATH, "//p[@class = 'input__error text_type_main-default']") # Уведомление об ошибке
    REG_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]") # Кнопка «Зарегистрироваться»
    SIGN_IN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]") # Кнопка «Войти»
    ACCOUNT_BUTTON = (By.XPATH, ".//a[@href = '/account']") # Ссылка на «Личный Кабинет»
    CONSTRUCTOR = (By.XPATH, "//p[contains(text(), 'Конструктор')]") # Ссылка на «Конструктор»
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]") # Кнопка «Оформить заказ»
    EXIT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]") # Кнопка «Выход»
    USERNAME = (By.XPATH, ".//input[@name='name']") # Имя пользователя
    PASSWORD = (By.XPATH, ".//input[@name='Пароль']") # Пароль
    ACTIVE_SECTION = (By.CSS_SELECTOR, ".tab_tab_type_current__2BEPc>span") # Активный раздел в блоке «Соберите бургер»
    SAUCES_SECTION = (By.XPATH, "//span[contains(text(),'Соусы')]") # Раздел «Соусы»
    BUNS_SECTION = (By.XPATH, "//span[contains(text(),'Булки')]") # Раздел «Булки»
    STUFFING_SECTION = (By.XPATH, "//span[contains(text(),'Начинки')]") # Раздел «Начинки»
    LOGIN_FORM_TITLE = (By.XPATH, "//h2[contains(text(),'Вход')]")  # Заголовок формы авторизации
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") # Логотип






